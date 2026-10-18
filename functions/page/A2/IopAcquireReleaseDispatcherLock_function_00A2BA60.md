# IopAcquireReleaseDispatcherLock

- RVA: `0x00A2BA60`–`0x00A2BAA6` (길이 `70` bytes)
- VA: `0x0000000140A2BA60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC384`
- 디코드: `19`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A2BA8D` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00A2BA9A` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00A2BA9F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [IopPassiveInterruptWorker](../../text/45/IopPassiveInterruptWorker_function_0045F3A0.md) at `0x0045F3C7`
- [IopPassiveInterruptWorker](../../text/45/IopPassiveInterruptWorker_function_0045F3A0.md) at `0x0045F455`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A2BA8D` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00A2BA9A` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x00A2BA9F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A2BA60  48 83 EC 38                     sub rsp, 0x38
00A2BA64  48 81 C1 A8 00 00 00            add rcx, 0xa8
00A2BA6B  45 33 C0                        xor r8d, r8d
00A2BA6E  84 D2                           test dl, dl
00A2BA70  74 26                           je 0x140a2ba98
00A2BA72  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A2BA7B  45 33 C9                        xor r9d, r9d
00A2BA7E  4C 21 44 24 20                  and qword ptr [rsp + 0x20], r8
00A2BA83  33 D2                           xor edx, edx
00A2BA85  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00A2BA8C  90                              nop
00A2BA8D  E8 1E 2C 7E FF                  call 0x14020e6b0
00A2BA92  48 83 C4 38                     add rsp, 0x38
00A2BA96  C3                              ret
00A2BA97  CC                              int3
00A2BA98  33 D2                           xor edx, edx
00A2BA9A  E8 71 38 91 FF                  call 0x14033f310
00A2BA9F  E8 0C 1E 83 FF                  call 0x14025d8b0
00A2BAA4  EB EC                           jmp 0x140a2ba92
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopAcquireReleaseDispatcherLock(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    a1 = (a1) + (168);
    a3 = 0;
    if ((unsigned __int8)(a2) == 0) goto loc_00A2BA98;
    a4 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(a1, a2, a3, a4);
loc_00A2BA92:
    v_rsp = (v_rsp) + (56);
    return result;
loc_00A2BA98:
    a2 = 0;
    result = KeSetEvent(a1, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1, a2, a3, a4);
    goto loc_00A2BA92;
}
```

## 5. (Beta) C Style

```c
int64_t IopAcquireReleaseDispatcherLock(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    Arg1 = (Arg1) + (168);
    Arg3 = 0;
    if ((uint8_t)(Arg2) == 0) goto loc_00A2BA98;
    Arg4 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(Arg1, Arg2, Arg3, Arg4);
loc_00A2BA92:
    local_rsp = (local_rsp) + (56);
    return result;
loc_00A2BA98:
    Arg2 = 0;
    result = KeSetEvent(Arg1, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegion(Arg1, Arg2, Arg3, Arg4);
    goto loc_00A2BA92;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A2BA60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A2BA60[BB_00A2BA60]
  bb_00A2BA72[BB_00A2BA72]
  bb_00A2BA92[BB_00A2BA92]
  bb_00A2BA97[BB_00A2BA97]
  bb_00A2BA98[BB_00A2BA98]
  bb_00A2BA60 -->|branch| bb_00A2BA98
  bb_00A2BA60 -->|fallthrough| bb_00A2BA72
  bb_00A2BA72 -->|flow| bb_00A2BA92
  bb_00A2BA97 -->|flow| bb_00A2BA98
  bb_00A2BA98 -->|branch| bb_00A2BA92
```
