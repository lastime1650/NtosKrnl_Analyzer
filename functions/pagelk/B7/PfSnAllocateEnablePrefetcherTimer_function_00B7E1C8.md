# PfSnAllocateEnablePrefetcherTimer

- RVA: `0x00B7E1C8`–`0x00B7E21F` (길이 `87` bytes)
- VA: `0x0000000140B7E1C8`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `24`개 명령, `87/87` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B7E1E2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B7E1F2` → [KeInitializeTimer](../../text/45/KeInitializeTimer_function_0045B590.md) (function, `0x0045B590`)
- `0x00B7E205` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (function, `0x0045BBD0`)

### Direct callers
- [PfSnQueueEnablePrefetcherTimer](../../page/75/PfSnQueueEnablePrefetcherTimer_function_00751E60.md) at `0x00751E72`
- [PfSnBeginBootPhase](../B6/PfSnBeginBootPhase_function_00B6BAC4.md) at `0x00B6BB02`

### Static image references
- `0x00B7E1FE` → RVA `0x005CDDC0` (`PfSnEnablePrefetcherTimerRoutine`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00B7E1E2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGELK` → `POOLCODE`)
  - `0x00B7E1F2` → [KeInitializeTimer](../../text/45/KeInitializeTimer_function_0045B590.md) (`PAGELK` → `.text`)
  - `0x00B7E205` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B7E1C8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00B7E1CD  57                              push rdi
00B7E1CE  48 83 EC 20                     sub rsp, 0x20
00B7E1D2  BA 88 00 00 00                  mov edx, 0x88
00B7E1D7  8B F9                           mov edi, ecx
00B7E1D9  41 B8 43 63 50 77               mov r8d, 0x77506343
00B7E1DF  8D 4A B8                        lea ecx, [rdx - 0x48]
00B7E1E2  E8 09 3F 00 00                  call 0x140b820f0
00B7E1E7  48 8B D8                        mov rbx, rax
00B7E1EA  48 85 C0                        test rax, rax
00B7E1ED  74 21                           je 0x140b7e210
00B7E1EF  48 8B C8                        mov rcx, rax
00B7E1F2  E8 99 D3 8D FF                  call 0x14045b590
00B7E1F7  48 8D 4B 40                     lea rcx, [rbx + 0x40]
00B7E1FB  4C 8B C3                        mov r8, rbx
00B7E1FE  48 8D 15 BB FB A4 FF            lea rdx, [rip - 0x5b0445]
00B7E205  E8 C6 D9 8D FF                  call 0x14045bbd0
00B7E20A  89 BB 80 00 00 00               mov dword ptr [rbx + 0x80], edi
00B7E210  48 8B C3                        mov rax, rbx
00B7E213  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00B7E218  48 83 C4 20                     add rsp, 0x20
00B7E21C  5F                              pop rdi
00B7E21D  C3                              ret
00B7E21E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfSnAllocateEnablePrefetcherTimer(int a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = ExAllocatePool2(136 - 72, 136, (unsigned int)(0x77506343ULL), a4);
    if (result != 0) {
        a1 = result;
        result = KeInitializeTimer(a1, 136, (unsigned int)(0x77506343ULL), a4);
        a1 = result + 64;
        a3 = result;
        a2 = v_rip - 5964869;
        result = KeInitializeDpc(a1, a2, a3, a4);
        *(unsigned int *)(result + 128) = (unsigned int)((unsigned int)(a1));
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfSnAllocateEnablePrefetcherTimer(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = ExAllocatePool2(136 - 72, 136, (uint32_t)(0x77506343ULL), a4);
    if (result != 0) {
        Arg1 = result;
        result = KeInitializeTimer(Arg1, 136, (uint32_t)(0x77506343ULL), a4);
        Arg1 = result + 64;
        a3 = result;
        a2 = v_rip - 5964869;
        result = KeInitializeDpc(Arg1, a2, a3, a4);
        *(uint32_t *)(result + 0x80) = (uint32_t)((uint32_t)(Arg1));
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B7E1C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B7E1C8[BB_00B7E1C8]
  bb_00B7E1EF[BB_00B7E1EF]
  bb_00B7E210[BB_00B7E210]
  bb_00B7E21E[BB_00B7E21E]
  bb_00B7E1C8 -->|branch| bb_00B7E210
  bb_00B7E1C8 -->|fallthrough| bb_00B7E1EF
  bb_00B7E1EF -->|flow| bb_00B7E210
```
