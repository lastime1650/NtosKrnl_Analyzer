# WmipFindRegEntryByDevice

- RVA: `0x0046C22C`–`0x0046C2A5` (길이 `121` bytes)
- VA: `0x000000014046C22C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C80`
- 디코드: `31`개 명령, `121/121` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0046C24A` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0046C256` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0046C261` → [WmipDoFindRegEntryByDevice](WmipDoFindRegEntryByDevice_function_0046C2F8.md) (function, `0x0046C2F8`)
- `0x0046C27C` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x0046C296` → [KeReleaseMutantEx](../39/KeReleaseMutantEx_function_00396850.md) (function, `0x00396850`)

### Direct callers
- [WmipRegisterDevice](../../page/9E/WmipRegisterDevice_function_009E2808.md) at `0x009E2860`
- [WmipUpdateRegistration](../../page/9E/WmipUpdateRegistration_function_009E2BA4.md) at `0x009E2BAE`
- [IoWMIRegistrationControl](../../page/9E/IoWMIRegistrationControl_function_009E2D60.md) at `0x009E2E30`
- [WmipDeregisterDevice](../../page/A7/WmipDeregisterDevice_function_00A7F9D4.md) at `0x00A7FA08`
- [sub_00B3C216](../../page/B3/Unknown_function_00B3C216.md) at `0x00B3C323`
- [sub_00B3C216](../../page/B3/Unknown_function_00B3C216.md) at `0x00B3C3A6`

### Static image references
- `0x0046C23B` → RVA `0x00EFFA60` (`.data`; read)
- `0x0046C24F` → RVA `0x00EFFC28` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0046C22C  40 53                           push rbx
0046C22E  48 83 EC 30                     sub rsp, 0x30
0046C232  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0046C238  48 8B D9                        mov rbx, rcx
0046C23B  48 8D 0D 1E 38 A9 00            lea rcx, [rip + 0xa9381e]
0046C242  45 33 C9                        xor r9d, r9d
0046C245  45 33 C0                        xor r8d, r8d
0046C248  33 D2                           xor edx, edx
0046C24A  E8 61 24 DA FF                  call 0x14020e6b0
0046C24F  48 8D 0D D2 39 A9 00            lea rcx, [rip + 0xa939d2]
0046C256  E8 15 C2 D9 FF                  call 0x140208470
0046C25B  48 8B CB                        mov rcx, rbx
0046C25E  44 8A C0                        mov r8b, al
0046C261  E8 92 00 00 00                  call 0x14046c2f8
0046C266  48 8B D8                        mov rbx, rax
0046C269  48 85 C0                        test rax, rax
0046C26C  74 04                           je 0x14046c272
0046C26E  F0 FF 40 30                     lock inc dword ptr [rax + 0x30]
0046C272  41 8A D0                        mov dl, r8b
0046C275  48 8D 0D AC 39 A9 00            lea rcx, [rip + 0xa939ac]
0046C27C  E8 1F 69 F2 FF                  call 0x140392ba0
0046C281  BA 01 00 00 00                  mov edx, 1
0046C286  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
0046C28B  48 8D 0D CE 37 A9 00            lea rcx, [rip + 0xa937ce]
0046C292  44 8D 42 03                     lea r8d, [rdx + 3]
0046C296  E8 B5 A5 F2 FF                  call 0x140396850
0046C29B  48 8B C3                        mov rax, rbx
0046C29E  48 83 C4 30                     add rsp, 0x30
0046C2A2  5B                              pop rbx
0046C2A3  C3                              ret
0046C2A4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WmipFindRegEntryByDevice(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (48);
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 11089950, a2, a3, a4);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11090386, a2, a3, a4);
    result = WmipDoFindRegEntryByDevice(a1, a2, (unsigned __int8)(result), a4);
    if (result != 0) {
    }
    result = KeReleaseSpinLock(v_rip + 11090348, (unsigned __int8)((unsigned __int8)(result)), (unsigned __int8)(result), a4);
    result = KeReleaseMutantEx(v_rip + 11089870, 1, 1 + 3, v_stack_p10);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WmipFindRegEntryByDevice(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (48);
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 11089950, Arg2, Arg3, Arg4);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11090386, Arg2, Arg3, Arg4);
    result = WmipDoFindRegEntryByDevice(Arg1, Arg2, (uint8_t)(result), Arg4);
    if (result != 0) {
    }
    result = KeReleaseSpinLock(v_rip + 11090348, (uint8_t)((uint8_t)(result)), (uint8_t)(result), Arg4);
    result = KeReleaseMutantEx(v_rip + 11089870, 1, 1 + 3, v_stack_p10);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0046C22C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0046C22C[BB_0046C22C]
  bb_0046C26E[BB_0046C26E]
  bb_0046C272[BB_0046C272]
  bb_0046C2A4[BB_0046C2A4]
  bb_0046C22C -->|branch| bb_0046C272
  bb_0046C22C -->|fallthrough| bb_0046C26E
  bb_0046C26E -->|flow| bb_0046C272
```
