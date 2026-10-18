# PspLockProcessShared

- RVA: `0x004016D0`–`0x0040172C` (길이 `92` bytes)
- VA: `0x00000001404016D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068D5C`
- 디코드: `28`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004016F1` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00401712` → [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [PsSwapProcessWorkingSet](../../page/78/PsSwapProcessWorkingSet_function_00781C24.md) at `0x00781C6A`
- [PspApplyCoreIsolationPolicy](../../page/78/PspApplyCoreIsolationPolicy_function_00783E48.md) at `0x00783E6B`
- [PspAssignPrimaryToken](../../page/78/PspAssignPrimaryToken_function_00784870.md) at `0x00784971`
- [DbgkForwardException](../../page/8A/DbgkForwardException_function_008A2D60.md) at `0x008A2FE4`
- [PspGetPreviousProcessThread](../../page/8C/PspGetPreviousProcessThread_function_008C9A68.md) at `0x008C9AA2`
- [NtSetInformationThread](../../page/8C/NtSetInformationThread_function_008C9F60.md) at `0x008CB1CD`
- [PsCaptureExceptionPort](../../page/90/PsCaptureExceptionPort_function_00904CB0.md) at `0x00904CD9`
- [PspInheritSyscallProvider](../../page/94/PspInheritSyscallProvider_function_00947F68.md) at `0x00947FBF`
- [NtQueryInformationProcess](../../page/9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AD086`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004016D0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
004016D5  57                              push rdi
004016D6  48 83 EC 20                     sub rsp, 0x20
004016DA  66 FF 8A E4 01 00 00            dec word ptr [rdx + 0x1e4]
004016E1  48 8D B9 C8 01 00 00            lea rdi, [rcx + 0x1c8]
004016E8  48 8B CF                        mov rcx, rdi
004016EB  45 33 C0                        xor r8d, r8d
004016EE  33 D2                           xor edx, edx
004016F0  90                              nop
004016F1  E8 3A EB E0 FF                  call 0x140210230
004016F6  48 8B D8                        mov rbx, rax
004016F9  B9 11 00 00 00                  mov ecx, 0x11
004016FE  33 C0                           xor eax, eax
00401700  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
00401705  74 10                           je 0x140401717
00401707  4C 8B CF                        mov r9, rdi
0040170A  4C 8B C3                        mov r8, rbx
0040170D  33 D2                           xor edx, edx
0040170F  48 8B CF                        mov rcx, rdi
00401712  E8 35 ED E0 FF                  call 0x14021044c
00401717  48 85 DB                        test rbx, rbx
0040171A  74 04                           je 0x140401720
0040171C  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00401720  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
00401725  48 83 C4 20                     add rsp, 0x20
00401729  5F                              pop rdi
0040172A  C3                              ret
0040172B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspLockProcessShared(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 456, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1 + 456;
        a3 = 0;
        a2 = 0;
        a1 = a1 + 456;
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
int64_t PspLockProcessShared(void *Arg1, void *Arg2, int32_t Arg3)
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
    result = KeAbPreAcquire(Arg1 + 456, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = Arg1 + 456;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1 + 456;
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
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x1C8` | `64` | `R` |
| `Arg2` | `+ 0x1E4` | `16` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004016D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004016D0[BB_004016D0]
  bb_00401707[BB_00401707]
  bb_00401717[BB_00401717]
  bb_0040171C[BB_0040171C]
  bb_00401720[BB_00401720]
  bb_0040172B[BB_0040172B]
  bb_004016D0 -->|branch| bb_00401717
  bb_004016D0 -->|fallthrough| bb_00401707
  bb_00401707 -->|flow| bb_00401717
  bb_00401717 -->|branch| bb_00401720
  bb_00401717 -->|fallthrough| bb_0040171C
  bb_0040171C -->|flow| bb_00401720
```
