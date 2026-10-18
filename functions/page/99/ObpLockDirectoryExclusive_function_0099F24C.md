# ObpLockDirectoryExclusive

- RVA: `0x0099F24C`–`0x0099F2B0` (길이 `100` bytes)
- VA: `0x000000014099F24C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `28`개 명령, `100/100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0099F27D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0099F296` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [ObpLookupObjectName](../89/ObpLookupObjectName_function_0089BE90.md) at `0x0089D5CA`
- [ObpMarkDirectoryObjectsTemporary](ObpMarkDirectoryObjectsTemporary_function_0099F00C.md) at `0x0099F03F`
- [ObCreateObjectTypeEx](../AB/ObCreateObjectTypeEx_function_00AB46D0.md) at `0x00AB482A`
- [sub_00B334D2](../B3/Unknown_function_00B334D2.md) at `0x00B33563`
- [sub_00B334D2](../B3/Unknown_function_00B334D2.md) at `0x00B3361C`
- [ObInitSystem](../../init/C7/ObInitSystem_function_00C71C7C.md) at `0x00C72264`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0099F27D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0099F296` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0099F24C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0099F251  57                              push rdi
0099F252  48 83 EC 20                     sub rsp, 0x20
0099F256  48 89 11                        mov qword ptr [rcx], rdx
0099F259  48 8D BA 28 01 00 00            lea rdi, [rdx + 0x128]
0099F260  C6 41 15 01                     mov byte ptr [rcx + 0x15], 1
0099F264  45 33 C0                        xor r8d, r8d
0099F267  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0099F270  33 D2                           xor edx, edx
0099F272  48 8B CF                        mov rcx, rdi
0099F275  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0099F27C  90                              nop
0099F27D  E8 AE 0F 87 FF                  call 0x140210230
0099F282  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0099F288  48 8B D8                        mov rbx, rax
0099F28B  73 0E                           jae 0x14099f29b
0099F28D  4C 8B C7                        mov r8, rdi
0099F290  48 8B D0                        mov rdx, rax
0099F293  48 8B CF                        mov rcx, rdi
0099F296  E8 F5 09 87 FF                  call 0x14020fc90
0099F29B  48 85 DB                        test rbx, rbx
0099F29E  74 04                           je 0x14099f2a4
0099F2A0  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0099F2A4  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0099F2A9  48 83 C4 20                     add rsp, 0x20
0099F2AD  5F                              pop rdi
0099F2AE  C3                              ret
0099F2AF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpLockDirectoryExclusive(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    *(unsigned __int64 *)(a1) = a2;
    *(unsigned __int8 *)(a1 + 21) = 1;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a2 + 296, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a2 + 296;
        a2 = result;
        a1 = a2 + 296;
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
int64_t ObpLockDirectoryExclusive(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    *(void **)(arg1) = Arg2;
    *(uint8_t *)(arg1 + 0x15) = 1;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg2 + 296, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg2 + 296;
        Arg2 = result;
        Arg1 = Arg2 + 296;
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
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x15` | `8` | `W` |
| `Arg2` | `+ 0x0` | `64` | `R/W` |
| `Arg2` | `+ 0x128` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0099F24C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0099F24C[BB_0099F24C]
  bb_0099F28D[BB_0099F28D]
  bb_0099F29B[BB_0099F29B]
  bb_0099F2A0[BB_0099F2A0]
  bb_0099F2A4[BB_0099F2A4]
  bb_0099F2AF[BB_0099F2AF]
  bb_0099F24C -->|branch| bb_0099F29B
  bb_0099F24C -->|fallthrough| bb_0099F28D
  bb_0099F28D -->|flow| bb_0099F29B
  bb_0099F29B -->|branch| bb_0099F2A4
  bb_0099F29B -->|fallthrough| bb_0099F2A0
  bb_0099F2A0 -->|flow| bb_0099F2A4
```
