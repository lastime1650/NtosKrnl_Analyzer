# VfRemLockReportBadReleaseAndWaitTag

- RVA: `0x00BA287C`–`0x00BA28B0` (길이 `52` bytes)
- VA: `0x0000000140BA287C`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `13`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA28A0` → [CarReportRuleViolationFromNt](../B9/CarReportRuleViolationFromNt_function_00B9D904.md) (function, `0x00B9D904`)

### Direct callers
- [IoReleaseRemoveLockAndWaitEx](../../text/4B/IoReleaseRemoveLockAndWaitEx_function_004B17B0.md) at `0x004B1855`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA287C  48 83 EC 48                     sub rsp, 0x48
00BA2880  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
00BA2885  4C 8B CA                        mov r9, rdx
00BA2888  BA D6 00 00 00                  mov edx, 0xd6
00BA288D  C7 44 24 28 0B 00 00 00         mov dword ptr [rsp + 0x28], 0xb
00BA2895  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00BA289A  4C 8B C1                        mov r8, rcx
00BA289D  8D 4A EE                        lea ecx, [rdx - 0x12]
00BA28A0  E8 5F B0 FF FF                  call 0x140b9d904
00BA28A5  B8 01 00 00 00                  mov eax, 1
00BA28AA  48 83 C4 48                     add rsp, 0x48
00BA28AE  C3                              ret
00BA28AF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfRemLockReportBadReleaseAndWaitTag(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m18 = a4;
    v_stack_m20 = 11;
    v_stack_m28 = a3;
    result = CarReportRuleViolationFromNt(214 - 18, 214, a1, a2);
    v_rsp = (v_rsp) + (72);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t VfRemLockReportBadReleaseAndWaitTag(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m18 = Arg4;
    v_stack_m20 = 11;
    v_stack_m28 = Arg3;
    result = CarReportRuleViolationFromNt(214 - 18, 214, Arg1, Arg2);
    local_rsp = (local_rsp) + (72);
    return 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA287C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA287C[BB_00BA287C]
  bb_00BA28AF[BB_00BA28AF]
```
