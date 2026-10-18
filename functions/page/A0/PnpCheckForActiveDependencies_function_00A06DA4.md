# PnpCheckForActiveDependencies

- RVA: `0x00A06DA4`–`0x00A06E0C` (길이 `104` bytes)
- VA: `0x0000000140A06DA4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000809AC`
- 디코드: `30`개 명령, `104/104` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A06DB3` → [PipIsDevNodeDNStarted](../../text/47/PipIsDevNodeDNStarted_function_00470870.md) (function, `0x00470870`)
- `0x00A06DE4` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00A06DF2` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00A06DFC` → [PipCheckForUnsatisfiedDependencies](PipCheckForUnsatisfiedDependencies_function_00A06E44.md) (function, `0x00A06E44`)
- `0x00A06E03` → [PnpReleaseDependencyRelationsLock](PnpReleaseDependencyRelationsLock_function_00A06E14.md) (function, `0x00A06E14`)

### Direct callers
- [PipProcessDevNodeTree](../8F/PipProcessDevNodeTree_function_008F9068.md) at `0x008F91A8`
- [PipProcessDevNodeTree](../8F/PipProcessDevNodeTree_function_008F9068.md) at `0x008F9652`
- [PiProcessQueryDeviceState](../8F/PiProcessQueryDeviceState_function_008FA0F8.md) at `0x008FA200`

### Static image references
- `0x00A06DD3` → RVA `0x00F8C560` (`.data`; read)
- `0x00A06DEB` → RVA `0x00F8CEA0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A06DB3` → [PipIsDevNodeDNStarted](../../text/47/PipIsDevNodeDNStarted_function_00470870.md) (`PAGE` → `.text`)
  - `0x00A06DE4` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00A06DF2` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A06DA4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A06DA9  57                              push rdi
00A06DAA  48 83 EC 20                     sub rsp, 0x20
00A06DAE  8B FA                           mov edi, edx
00A06DB0  48 8B D9                        mov rbx, rcx
00A06DB3  E8 B8 9A A6 FF                  call 0x140470870
00A06DB8  85 C0                           test eax, eax
00A06DBA  74 0E                           je 0x140a06dca
00A06DBC  32 C0                           xor al, al
00A06DBE  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A06DC3  48 83 C4 20                     add rsp, 0x20
00A06DC7  5F                              pop rdi
00A06DC8  C3                              ret
00A06DC9  CC                              int3
00A06DCA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A06DD3  48 8D 0D 86 57 58 00            lea rcx, [rip + 0x585786]
00A06DDA  B2 01                           mov dl, 1
00A06DDC  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00A06DE3  90                              nop
00A06DE4  E8 D7 AD 80 FF                  call 0x140211bc0
00A06DE9  B2 01                           mov dl, 1
00A06DEB  48 8D 0D AE 60 58 00            lea rcx, [rip + 0x5860ae]
00A06DF2  E8 C9 AD 80 FF                  call 0x140211bc0
00A06DF7  8B D7                           mov edx, edi
00A06DF9  48 8B CB                        mov rcx, rbx
00A06DFC  E8 43 00 00 00                  call 0x140a06e44
00A06E01  8A D8                           mov bl, al
00A06E03  E8 0C 00 00 00                  call 0x140a06e14
00A06E08  8A C3                           mov al, bl
00A06E0A  EB B2                           jmp 0x140a06dbe
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpCheckForActiveDependencies(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = PipIsDevNodeDNStarted(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00A06DCA;
    result = 0;
loc_00A06DBE:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A06DCA:
    result = ExAcquireResourceSharedLite(v_rip + 5789574, 1, a3, a4);
    result = ExAcquireResourceSharedLite(v_rip + 5791918, 1, a3, a4);
    result = PipCheckForUnsatisfiedDependencies(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    result = PnpReleaseDependencyRelationsLock(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    goto loc_00A06DBE;
}
```

## 5. (Beta) C Style

```c
int64_t PnpCheckForActiveDependencies(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = PipIsDevNodeDNStarted(Arg1, Arg2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_00A06DCA;
    result = 0;
loc_00A06DBE:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A06DCA:
    result = ExAcquireResourceSharedLite(v_rip + 5789574, 1, a3, a4);
    result = ExAcquireResourceSharedLite(v_rip + 5791918, 1, a3, a4);
    result = PipCheckForUnsatisfiedDependencies(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    result = PnpReleaseDependencyRelationsLock(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    goto loc_00A06DBE;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A06DA4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A06DA4[BB_00A06DA4]
  bb_00A06DBC[BB_00A06DBC]
  bb_00A06DBE[BB_00A06DBE]
  bb_00A06DC9[BB_00A06DC9]
  bb_00A06DCA[BB_00A06DCA]
  bb_00A06DA4 -->|branch| bb_00A06DCA
  bb_00A06DA4 -->|fallthrough| bb_00A06DBC
  bb_00A06DBC -->|flow| bb_00A06DBE
  bb_00A06DC9 -->|flow| bb_00A06DCA
  bb_00A06DCA -->|branch| bb_00A06DBE
```
