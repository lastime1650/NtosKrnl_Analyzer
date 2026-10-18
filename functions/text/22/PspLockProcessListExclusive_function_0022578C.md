# PspLockProcessListExclusive

- RVA: `0x0022578C`–`0x002257E0` (길이 `84` bytes)
- VA: `0x000000014022578C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `22`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **19**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x002257A6` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x002257CB` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [PspDetachSession](PspDetachSession_function_0022480C.md) at `0x00224839`
- [PsGetSessionObjectById](PsGetSessionObjectById_function_002250C0.md) at `0x002250FA`
- [PsGetSessionById](PsGetSessionById_function_00225150.md) at `0x0022517C`
- [PsAttachSession](../5E/PsAttachSession_function_005E4F40.md) at `0x005E4F6D`
- [PsIsSessionInCurrentServerSilo](../5E/PsIsSessionInCurrentServerSilo_function_005E4FE8.md) at `0x005E5024`
- [PspInitializeSessionGlobals](../../page/70/PspInitializeSessionGlobals_function_007005B8.md) at `0x00700615`
- [PspInitializeSessionGlobals](../../page/70/PspInitializeSessionGlobals_function_007005B8.md) at `0x00700660`
- [PspAttachSession](../../page/78/PspAttachSession_function_00788EB0.md) at `0x00788EFA`
- [PspDereferenceSessionFinal](../../page/78/PspDereferenceSessionFinal_function_00788F5C.md) at `0x00788F93`
- [PspDereferenceSessionFinal](../../page/78/PspDereferenceSessionFinal_function_00788F5C.md) at `0x0078904C`
- [PspFreeSessionId](../../page/78/PspFreeSessionId_function_007890B8.md) at `0x007890D0`
- [PspGetNewSessionId](../../page/78/PspGetNewSessionId_function_00789108.md) at `0x00789128`
- [PspMarkSessionReferenceProcess](../../page/78/PspMarkSessionReferenceProcess_function_00789220.md) at `0x00789253`
- [PspUnlinkSessionId](../../page/78/PspUnlinkSessionId_function_007895D8.md) at `0x007895F1`
- [PspProcessDelete](../../page/90/PspProcessDelete_function_00907B90.md) at `0x00907C09`
- [PsGetNextSession](../../page/91/PsGetNextSession_function_009128C0.md) at `0x00912906`
- [PspInsertProcess](../../page/94/PspInsertProcess_function_009472CC.md) at `0x0094736D`
- [PsJoinSession](../../page/A5/PsJoinSession_function_00A5F118.md) at `0x00A5F150`
- [PsUnlinkProcessFromSession](../../page/A8/PsUnlinkProcessFromSession_function_00A8AA88.md) at `0x00A8AAA1`
- [PsSessionSetUnloadAddress](../../page/AA/PsSessionSetUnloadAddress_function_00AABECC.md) at `0x00AABF0E`
- [PspMakeSessionVisible](../../page/AC/PspMakeSessionVisible_function_00ACA0B8.md) at `0x00ACA0D1`

### Static image references
- `0x0022579C` → RVA `0x00FD9AF8` (`PAGEDATA`; read)
- `0x002257AB` → RVA `0x00FD9AF8` (`PAGEDATA`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0022578C  40 53                           push rbx
0022578E  48 83 EC 20                     sub rsp, 0x20
00225792  66 FF 89 E6 01 00 00            dec word ptr [rcx + 0x1e6]
00225799  45 33 C0                        xor r8d, r8d
0022579C  48 8D 0D 55 43 DB 00            lea rcx, [rip + 0xdb4355]
002257A3  33 D2                           xor edx, edx
002257A5  90                              nop
002257A6  E8 85 AA FE FF                  call 0x140210230
002257AB  F0 48 0F BA 2D 43 43 DB 00 00   lock bts qword ptr [rip + 0xdb4343], 0
002257B5  48 8B D8                        mov rbx, rax
002257B8  73 16                           jae 0x1402257d0
002257BA  4C 8D 05 37 43 DB 00            lea r8, [rip + 0xdb4337]
002257C1  48 8B D0                        mov rdx, rax
002257C4  48 8D 0D 2D 43 DB 00            lea rcx, [rip + 0xdb432d]
002257CB  E8 C0 A4 FE FF                  call 0x14020fc90
002257D0  48 85 DB                        test rbx, rbx
002257D3  74 04                           je 0x1402257d9
002257D5  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
002257D9  48 83 C4 20                     add rsp, 0x20
002257DD  5B                              pop rbx
002257DE  C3                              ret
002257DF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspLockProcessListExclusive(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 14369621, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 14369591;
        a2 = result;
        a1 = v_rip + 14369581;
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
int64_t PspLockProcessListExclusive(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 14369621, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 14369591;
        Arg2 = result;
        Arg1 = v_rip + 14369581;
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
| `Arg1` | `+ 0x1E6` | `16` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0022578C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0022578C[BB_0022578C]
  bb_002257BA[BB_002257BA]
  bb_002257D0[BB_002257D0]
  bb_002257D5[BB_002257D5]
  bb_002257D9[BB_002257D9]
  bb_002257DF[BB_002257DF]
  bb_0022578C -->|branch| bb_002257D0
  bb_0022578C -->|fallthrough| bb_002257BA
  bb_002257BA -->|flow| bb_002257D0
  bb_002257D0 -->|branch| bb_002257D9
  bb_002257D0 -->|fallthrough| bb_002257D5
  bb_002257D5 -->|flow| bb_002257D9
```
