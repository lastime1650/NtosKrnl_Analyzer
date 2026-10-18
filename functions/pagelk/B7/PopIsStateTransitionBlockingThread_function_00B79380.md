# PopIsStateTransitionBlockingThread

- RVA: `0x00B79380`–`0x00B793D4` (길이 `84` bytes)
- VA: `0x0000000140B79380`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069370`
- 디코드: `22`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00B7938F` → [PopAcquireRwLockShared](../../text/2D/PopAcquireRwLockShared_function_002D9A40.md) (function, `0x002D9A40`)
- `0x00B793A6` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- [PopInvokeWin32Callout](../../page/91/PopInvokeWin32Callout_function_009125F4.md) at `0x0091263D`
- [PopNotifyConsoleUserPresent](../../page/91/PopNotifyConsoleUserPresent_function_00913C50.md) at `0x00913D1D`
- [PopPowerAggregatorNotifyCsStateExited](../../page/98/PopPowerAggregatorNotifyCsStateExited_function_0098A434.md) at `0x0098A519`

### Static image references
- `0x00B79386` → RVA `0x00F0DD88` (`.data`; read)
- `0x00B79394` → RVA `0x00F0DD80` (`.data`; read)
- `0x00B793C4` → RVA `0x00F0D180` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00B7938F` → [PopAcquireRwLockShared](../../text/2D/PopAcquireRwLockShared_function_002D9A40.md) (`PAGELK` → `.text`)
  - `0x00B793A6` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B79380  40 53                           push rbx
00B79382  48 83 EC 20                     sub rsp, 0x20
00B79386  48 8D 0D FB 49 39 00            lea rcx, [rip + 0x3949fb]
00B7938D  32 DB                           xor bl, bl
00B7938F  E8 AC 06 76 FF                  call 0x1402d9a40
00B79394  8B 05 E6 49 39 00               mov eax, dword ptr [rip + 0x3949e6]
00B7939A  83 F8 FF                        cmp eax, -1
00B7939D  75 15                           jne 0x140b793b4
00B7939F  48 8D 0D E2 49 39 00            lea rcx, [rip + 0x3949e2]
00B793A6  E8 11 68 76 FF                  call 0x1402dfbbc
00B793AB  8A C3                           mov al, bl
00B793AD  48 83 C4 20                     add rsp, 0x20
00B793B1  5B                              pop rbx
00B793B2  C3                              ret
00B793B3  CC                              int3
00B793B4  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
00B793BD  48 8D 04 40                     lea rax, [rax + rax*2]
00B793C1  48 03 C0                        add rax, rax
00B793C4  4C 8D 05 B5 3D 39 00            lea r8, [rip + 0x393db5]
00B793CB  49 3B 14 C0                     cmp rdx, qword ptr [r8 + rax*8]
00B793CF  0F 94 C3                        sete bl
00B793D2  EB CB                           jmp 0x140b7939f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopIsStateTransitionBlockingThread(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    result = PopAcquireRwLockShared(v_rip + 3754491, a2, a3, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3754470)))) != -1) goto loc_00B793B4;
loc_00B7939F:
    result = PopReleaseRwLock(v_rip + 3754466, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return 0;
loc_00B793B4:
    result = (0 + 0 * 2) + (0 + 0 * 2);
    v_rbx = ((*(unsigned __int64 *)(gs_base + (0 + 392))) == (*(unsigned __int64 *)(v_rip + 3751349 + result * 8))) ? 1 : 0;
    goto loc_00B7939F;
}
```

## 5. (Beta) C Style

```c
void PopIsStateTransitionBlockingThread(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    result = PopAcquireRwLockShared(v_rip + 3754491, a2, a3, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3949E6)))) != -1) goto loc_00B793B4;
loc_00B7939F:
    result = PopReleaseRwLock(v_rip + 3754466, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return 0;
loc_00B793B4:
    result = (0 + 0 * 2) + (0 + 0 * 2);
    local_rbx = ((*(uint64_t *)(gs_base + (0 + 0x188))) == (*(uint64_t *)(v_rip + 0x393DB5 + result * 8))) ? 1 : 0;
    goto loc_00B7939F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B79380&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B79380[BB_00B79380]
  bb_00B7939F[BB_00B7939F]
  bb_00B793B3[BB_00B793B3]
  bb_00B793B4[BB_00B793B4]
  bb_00B79380 -->|branch| bb_00B793B4
  bb_00B79380 -->|fallthrough| bb_00B7939F
  bb_00B793B3 -->|flow| bb_00B793B4
  bb_00B793B4 -->|branch| bb_00B7939F
```
