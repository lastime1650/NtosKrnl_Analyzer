# CcAcquireBcbLockAndVacbLock

- RVA: `0x0026FC58`–`0x0026FCB4` (길이 `92` bytes)
- VA: `0x000000014026FC58`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `28`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0026FC70` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x0026FC81` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0026FC9A` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [CcExtendVacbArray](CcExtendVacbArray_function_0026DCD0.md) at `0x0026DDE7`
- [CcExtendVacbArray](CcExtendVacbArray_function_0026DCD0.md) at `0x0026DFF8`
- [CcUnmapInactiveViewsInternal](../27/CcUnmapInactiveViewsInternal_function_0027174C.md) at `0x002719A3`
- [CcPinFileData](../33/CcPinFileData_function_0033FB40.md) at `0x00340C6F`
- [CcUnmapVacbArray](../38/CcUnmapVacbArray_function_0038AEAC.md) at `0x0038AF1C`
- [CcDereferenceFileOffset](../4E/CcDereferenceFileOffset_function_004E004C.md) at `0x004E006E`
- [sub_006E2024](../6E/Unknown_function_006E2024.md) at `0x006E2030`
- [sub_006E532A](../6E/Unknown_function_006E532A.md) at `0x006E5373`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0026FC58  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0026FC5D  57                              push rdi
0026FC5E  48 83 EC 20                     sub rsp, 0x20
0026FC62  48 8B FA                        mov rdi, rdx
0026FC65  85 C9                           test ecx, ecx
0026FC67  74 0C                           je 0x14026fc75
0026FC69  48 8D 8A 20 01 00 00            lea rcx, [rdx + 0x120]
0026FC70  E8 2B E9 F9 FF                  call 0x14020e5a0
0026FC75  48 83 C7 68                     add rdi, 0x68
0026FC79  45 33 C0                        xor r8d, r8d
0026FC7C  48 8B CF                        mov rcx, rdi
0026FC7F  33 D2                           xor edx, edx
0026FC81  E8 AA 05 FA FF                  call 0x140210230
0026FC86  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0026FC8C  48 8B D8                        mov rbx, rax
0026FC8F  73 0E                           jae 0x14026fc9f
0026FC91  4C 8B C7                        mov r8, rdi
0026FC94  48 8B D0                        mov rdx, rax
0026FC97  48 8B CF                        mov rcx, rdi
0026FC9A  E8 F1 FF F9 FF                  call 0x14020fc90
0026FC9F  48 85 DB                        test rbx, rbx
0026FCA2  74 04                           je 0x14026fca8
0026FCA4  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0026FCA8  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0026FCAD  48 83 C4 20                     add rsp, 0x20
0026FCB1  5F                              pop rdi
0026FCB2  C3                              ret
0026FCB3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcAcquireBcbLockAndVacbLock(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if (a1 != 0) {
        a1 = a2 + 288;
        result = ExAcquireFastMutex(a1, a2, a3, a4);
    }
    v_rdi = (a2) + (104);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rdi, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rdi;
        a2 = result;
        a1 = v_rdi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcAcquireBcbLockAndVacbLock(int32_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if (Arg1 != 0) {
        Arg1 = Arg2 + 288;
        result = ExAcquireFastMutex(Arg1, Arg2, Arg3, a4);
    }
    local_rdi = (Arg2) + (104);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rdi;
        Arg2 = result;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R/W` |
| `Arg2` | `+ 0x120` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0026FC58&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0026FC58[BB_0026FC58]
  bb_0026FC69[BB_0026FC69]
  bb_0026FC75[BB_0026FC75]
  bb_0026FC91[BB_0026FC91]
  bb_0026FC9F[BB_0026FC9F]
  bb_0026FCA4[BB_0026FCA4]
  bb_0026FCA8[BB_0026FCA8]
  bb_0026FCB3[BB_0026FCB3]
  bb_0026FC58 -->|branch| bb_0026FC75
  bb_0026FC58 -->|fallthrough| bb_0026FC69
  bb_0026FC69 -->|flow| bb_0026FC75
  bb_0026FC75 -->|branch| bb_0026FC9F
  bb_0026FC75 -->|fallthrough| bb_0026FC91
  bb_0026FC91 -->|flow| bb_0026FC9F
  bb_0026FC9F -->|branch| bb_0026FCA8
  bb_0026FC9F -->|fallthrough| bb_0026FCA4
  bb_0026FCA4 -->|flow| bb_0026FCA8
```
