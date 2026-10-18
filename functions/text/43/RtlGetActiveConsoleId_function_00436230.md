# RtlGetActiveConsoleId

- RVA: `0x00436230`–`0x00436260` (길이 `48` bytes)
- VA: `0x0000000140436230`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063CEC`
- 디코드: `13`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00436234` → [PsIsCurrentThreadInServerSilo](PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x0043624F` → [PsGetCurrentServerSiloGlobals](../2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)

### Direct callers
- [PoBlockConsoleSwitchEx](PoBlockConsoleSwitchEx_function_00435CD4.md) at `0x00435D1D`
- [PoBlockConsoleSwitchEx](PoBlockConsoleSwitchEx_function_00435CD4.md) at `0x00435D42`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x008A02CA`
- [PopNotifyConsoleUserPresent](../../page/91/PopNotifyConsoleUserPresent_function_00913C50.md) at `0x00913CB5`
- [PiCMQueryRemove](../../page/AD/PiCMQueryRemove_function_00AD43F4.md) at `0x00AD4651`
- [sub_00B47AE6](../../page/B4/Unknown_function_00B47AE6.md) at `0x00B47AF6`
- [sub_00B47AE6](../../page/B4/Unknown_function_00B47AE6.md) at `0x00B47BCA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00436230  48 83 EC 28                     sub rsp, 0x28
00436234  E8 A7 00 00 00                  call 0x1404362e0
00436239  84 C0                           test al, al
0043623B  75 12                           jne 0x14043624f
0043623D  48 B8 D8 02 00 00 80 F7 FF FF   movabs rax, 0xfffff780000002d8
00436247  8B 00                           mov eax, dword ptr [rax]
00436249  48 83 C4 28                     add rsp, 0x28
0043624D  C3                              ret
0043624E  CC                              int3
0043624F  E8 9C 7F EC FF                  call 0x1402fe1f0
00436254  48 8B 80 08 05 00 00            mov rax, qword ptr [rax + 0x508]
0043625B  8B 40 04                        mov eax, dword ptr [rax + 4]
0043625E  EB E9                           jmp 0x140436249
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlGetActiveConsoleId(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0043624F;
loc_00436249:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(*(unsigned int *)(result));
loc_0043624F:
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    goto loc_00436249;
}
```

## 5. (Beta) C Style

```c
void RtlGetActiveConsoleId(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_0043624F;
loc_00436249:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(*(uint32_t *)(result));
loc_0043624F:
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    goto loc_00436249;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00436230&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00436230[BB_00436230]
  bb_0043623D[BB_0043623D]
  bb_00436249[BB_00436249]
  bb_0043624E[BB_0043624E]
  bb_0043624F[BB_0043624F]
  bb_00436230 -->|branch| bb_0043624F
  bb_00436230 -->|fallthrough| bb_0043623D
  bb_0043623D -->|flow| bb_00436249
  bb_0043624E -->|flow| bb_0043624F
  bb_0043624F -->|branch| bb_00436249
```
