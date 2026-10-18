# MI_LOCK_RELOCATIONS_SHARED

- RVA: `0x0044A848`–`0x0044A8A1` (길이 `89` bytes)
- VA: `0x000000014044A848`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068D5C`
- 디코드: `28`개 명령, `89/89` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0044A866` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0044A887` → [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [MiUpdateImagePfnImportRelocations](MiUpdateImagePfnImportRelocations_function_00449E84.md) at `0x00449F75`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044A848  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0044A84D  57                              push rdi
0044A84E  48 83 EC 20                     sub rsp, 0x20
0044A852  66 FF 89 E6 01 00 00            dec word ptr [rcx + 0x1e6]
0044A859  48 8D 7A 18                     lea rdi, [rdx + 0x18]
0044A85D  48 8B CF                        mov rcx, rdi
0044A860  45 33 C0                        xor r8d, r8d
0044A863  33 D2                           xor edx, edx
0044A865  90                              nop
0044A866  E8 C5 59 DC FF                  call 0x140210230
0044A86B  48 8B D8                        mov rbx, rax
0044A86E  B9 11 00 00 00                  mov ecx, 0x11
0044A873  33 C0                           xor eax, eax
0044A875  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
0044A87A  74 10                           je 0x14044a88c
0044A87C  4C 8B CF                        mov r9, rdi
0044A87F  4C 8B C3                        mov r8, rbx
0044A882  33 D2                           xor edx, edx
0044A884  48 8B CF                        mov rcx, rdi
0044A887  E8 C0 5B DC FF                  call 0x14021044c
0044A88C  48 85 DB                        test rbx, rbx
0044A88F  74 04                           je 0x14044a895
0044A891  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0044A895  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0044A89A  48 83 C4 20                     add rsp, 0x20
0044A89E  5F                              pop rdi
0044A89F  C3                              ret
0044A8A0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MI_LOCK_RELOCATIONS_SHARED(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a2 + 24, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a2 + 24;
        a3 = 0;
        a2 = 0;
        a1 = a2 + 24;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
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
int64_t MI_LOCK_RELOCATIONS_SHARED(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg2 + 24, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = Arg2 + 24;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg2 + 24;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
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
| `Arg1` | `+ 0x1E6` | `16` | `R/W` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044A848&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044A848[BB_0044A848]
  bb_0044A87C[BB_0044A87C]
  bb_0044A88C[BB_0044A88C]
  bb_0044A891[BB_0044A891]
  bb_0044A895[BB_0044A895]
  bb_0044A8A0[BB_0044A8A0]
  bb_0044A848 -->|branch| bb_0044A88C
  bb_0044A848 -->|fallthrough| bb_0044A87C
  bb_0044A87C -->|flow| bb_0044A88C
  bb_0044A88C -->|branch| bb_0044A895
  bb_0044A88C -->|fallthrough| bb_0044A891
  bb_0044A891 -->|flow| bb_0044A895
```
