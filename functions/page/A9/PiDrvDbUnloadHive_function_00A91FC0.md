# PiDrvDbUnloadHive

- RVA: `0x00A91FC0`–`0x00A92005` (길이 `69` bytes)
- VA: `0x0000000140A91FC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B13B4`
- 디코드: `18`개 명령, `69/69` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A91FF3` → [ZwUnloadKeyEx](../../text/6B/ZwUnloadKeyEx_function_006B0C70.md) (function, `0x006B0C70`)
- `0x00A91FFE` → [ZwUnloadKey2](../../text/6B/ZwUnloadKey2_function_006B0C50.md) (function, `0x006B0C50`)

### Direct callers
- [PiDrvDbSetupNodeHive](../74/PiDrvDbSetupNodeHive_function_00743884.md) at `0x00743CCA`
- [PiDrvDbLoadNodeWorkerCallback](PiDrvDbLoadNodeWorkerCallback_function_00A91D40.md) at `0x00A91E86`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A91FF3` → [ZwUnloadKeyEx](../../text/6B/ZwUnloadKeyEx_function_006B0C70.md) (`PAGE` → `.text`)
  - `0x00A91FFE` → [ZwUnloadKey2](../../text/6B/ZwUnloadKey2_function_006B0C50.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A91FC0  4C 8B DC                        mov r11, rsp
00A91FC3  48 83 EC 58                     sub rsp, 0x58
00A91FC7  33 C0                           xor eax, eax
00A91FC9  49 89 4B D8                     mov qword ptr [r11 - 0x28], rcx
00A91FCD  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
00A91FD1  0F 57 C0                        xorps xmm0, xmm0
00A91FD4  49 C7 43 C8 30 00 00 00         mov qword ptr [r11 - 0x38], 0x30
00A91FDC  49 8D 4B C8                     lea rcx, [r11 - 0x38]
00A91FE0  49 C7 43 E0 40 02 00 00         mov qword ptr [r11 - 0x20], 0x240
00A91FE8  F3 0F 7F 44 24 40               movdqu xmmword ptr [rsp + 0x40], xmm0
00A91FEE  48 85 D2                        test rdx, rdx
00A91FF1  74 0B                           je 0x140a91ffe
00A91FF3  E8 78 EC C1 FF                  call 0x1406b0c70
00A91FF8  48 83 C4 58                     add rsp, 0x58
00A91FFC  C3                              ret
00A91FFD  CC                              int3
00A91FFE  E8 4D EC C1 FF                  call 0x1406b0c50
00A92003  EB F3                           jmp 0x140a91ff8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDrvDbUnloadHive(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (88);
    result = 0;
    *(unsigned __int64 *)(v_rsp - 40) = a1;
    *(unsigned __int64 *)(v_rsp - 48) = 0;
    *(unsigned __int64 *)(v_rsp - 56) = 48;
    *(unsigned __int64 *)(v_rsp - 32) = 576;
    v_stack_m18 = v_xmm0;
    if (a2 == 0) goto loc_00A91FFE;
    result = ZwUnloadKeyEx(v_rsp - 56, a2, a3, a4);
loc_00A91FF8:
    v_rsp = (v_rsp) + (88);
    return result;
loc_00A91FFE:
    result = ZwUnloadKey2(v_rsp - 56, a2, a3, a4);
    goto loc_00A91FF8;
}
```

## 5. (Beta) C Style

```c
int64_t PiDrvDbUnloadHive(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (88);
    result = 0;
    *(uint64_t *)(local_rsp - 0x28) = Arg1;
    *(uint64_t *)(local_rsp - 0x30) = 0;
    *(uint64_t *)(local_rsp - 0x38) = 48;
    *(uint64_t *)(local_rsp - 0x20) = 576;
    v_stack_m18 = v_xmm0;
    if (Arg2 == 0) goto loc_00A91FFE;
    result = ZwUnloadKeyEx(local_rsp - 56, Arg2, a3, a4);
loc_00A91FF8:
    local_rsp = (local_rsp) + (88);
    return result;
loc_00A91FFE:
    result = ZwUnloadKey2(local_rsp - 56, Arg2, a3, a4);
    goto loc_00A91FF8;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A91FC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A91FC0[BB_00A91FC0]
  bb_00A91FF3[BB_00A91FF3]
  bb_00A91FF8[BB_00A91FF8]
  bb_00A91FFD[BB_00A91FFD]
  bb_00A91FFE[BB_00A91FFE]
  bb_00A91FC0 -->|branch| bb_00A91FFE
  bb_00A91FC0 -->|fallthrough| bb_00A91FF3
  bb_00A91FF3 -->|flow| bb_00A91FF8
  bb_00A91FFD -->|flow| bb_00A91FFE
  bb_00A91FFE -->|branch| bb_00A91FF8
```
