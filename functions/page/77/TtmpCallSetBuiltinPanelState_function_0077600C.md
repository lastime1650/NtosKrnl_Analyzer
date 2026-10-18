# TtmpCallSetBuiltinPanelState

- RVA: `0x0077600C`–`0x00776083` (길이 `119` bytes)
- VA: `0x000000014077600C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C33C`
- 디코드: `35`개 명령, `119/119` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0077605D` → [TtmpStartCallout](TtmpStartCallout_function_00776AA4.md) (function, `0x00776AA4`)
- `0x00776066` → [PoSessionBuiltinPanelState](../../text/5D/PoSessionBuiltinPanelState_function_005DC420.md) (function, `0x005DC420`)
- `0x00776072` → [TtmpStopCallout](TtmpStopCallout_function_00776C24.md) (function, `0x00776C24`)

### Direct callers
- [TtmpPushTerminalDisplayStateOntoDevice](TtmpPushTerminalDisplayStateOntoDevice_function_00776838.md) at `0x00776870`
- [TtmpPushTerminalDisplayStateOntoDevice](TtmpPushTerminalDisplayStateOntoDevice_function_00776838.md) at `0x0077689B`
- [TtmpPushTerminalDisplayStateOntoDevice](TtmpPushTerminalDisplayStateOntoDevice_function_00776838.md) at `0x007768B1`

### Static image references
- `0x00776052` → RVA `0x005DC420` (`PoSessionBuiltinPanelState`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00776066` → [PoSessionBuiltinPanelState](../../text/5D/PoSessionBuiltinPanelState_function_005DC420.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077600C  4C 8B DC                        mov r11, rsp
0077600F  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00776013  57                              push rdi
00776014  48 83 EC 60                     sub rsp, 0x60
00776018  83 7A 10 01                     cmp dword ptr [rdx + 0x10], 1
0077601C  41 8B D8                        mov ebx, r8d
0077601F  48 8B F9                        mov rdi, rcx
00776022  75 53                           jne 0x140776077
00776024  8B 42 48                        mov eax, dword ptr [rdx + 0x48]
00776027  A8 01                           test al, 1
00776029  74 4C                           je 0x140776077
0077602B  0F 57 C0                        xorps xmm0, xmm0
0077602E  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
00776032  33 C0                           xor eax, eax
00776034  4C 8B C2                        mov r8, rdx
00776037  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
0077603C  48 8B D1                        mov rdx, rcx
0077603F  41 B9 05 00 00 00               mov r9d, 5
00776045  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
0077604A  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0077604E  49 8D 4B C8                     lea rcx, [r11 - 0x38]
00776052  48 8D 05 C7 63 E6 FF            lea rax, [rip - 0x199c39]
00776059  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
0077605D  E8 42 0A 00 00                  call 0x140776aa4
00776062  8B 17                           mov edx, dword ptr [rdi]
00776064  8B CB                           mov ecx, ebx
00776066  E8 B5 63 E6 FF                  call 0x1405dc420
0077606B  33 D2                           xor edx, edx
0077606D  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00776072  E8 AD 0B 00 00                  call 0x140776c24
00776077  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
0077607C  48 83 C4 60                     add rsp, 0x60
00776080  5F                              pop rdi
00776081  C3                              ret
00776082  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmpCallSetBuiltinPanelState(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    v_rsp = (v_rsp) - (96);
    if ((*(unsigned int *)(a2 + 16)) != 1) goto loc_00776077;
    result = (unsigned int)(*(unsigned int *)(a2 + 72));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 72)))) & (1)) != 0) {
        v_stack_m40 = (unsigned int)((unsigned int)(a3));
        result = 0;
        a3 = a2;
        v_stack_m38 = v_xmm0;
        a2 = a1;
        a4 = 5;
        v_stack_m28 = v_xmm0;
        *(unsigned __int64 *)(v_rsp - 24) = 0;
        a1 = v_rsp - 56;
        result = v_rip - 1678393;
        *(unsigned __int64 *)(v_rsp - 72) = result;
        result = TtmpStartCallout(a1, a2, a3, a4);
        a2 = *(unsigned int *)(a1);
        a1 = (unsigned int)((unsigned int)(a3));
        result = PoSessionBuiltinPanelState(a1, a2, a3, a4);
        a2 = 0;
        a1 = v_stack_m38;
        result = TtmpStopCallout(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmpCallSetBuiltinPanelState(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    local_rsp = (local_rsp) - (96);
    if ((*(uint32_t *)(arg2 + 0x10)) != 1) goto loc_00776077;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x48));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x48)))) & (1)) != 0) {
        v_stack_m40 = (uint32_t)((uint32_t)(Arg3));
        result = 0;
        Arg3 = Arg2;
        v_stack_m38 = v_xmm0;
        Arg2 = Arg1;
        a4 = 5;
        v_stack_m28 = v_xmm0;
        *(uint64_t *)(local_rsp - 0x18) = 0;
        Arg1 = local_rsp - 56;
        result = v_rip - 1678393;
        *(uint64_t *)(local_rsp - 0x48) = result;
        result = TtmpStartCallout(Arg1, Arg2, Arg3, a4);
        Arg2 = *(uint32_t *)(arg1);
        Arg1 = (uint32_t)((uint32_t)(Arg3));
        result = PoSessionBuiltinPanelState(Arg1, Arg2, Arg3, a4);
        Arg2 = 0;
        Arg1 = v_stack_m38;
        result = TtmpStopCallout(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (96);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x48` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077600C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077600C[BB_0077600C]
  bb_00776024[BB_00776024]
  bb_0077602B[BB_0077602B]
  bb_00776077[BB_00776077]
  bb_00776082[BB_00776082]
  bb_0077600C -->|branch| bb_00776077
  bb_0077600C -->|fallthrough| bb_00776024
  bb_00776024 -->|branch| bb_00776077
  bb_00776024 -->|fallthrough| bb_0077602B
  bb_0077602B -->|flow| bb_00776077
```
