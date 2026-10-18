# HalpBlkAllocateShadowCode

- RVA: `0x00C234A4`–`0x00C23523` (길이 `127` bytes)
- VA: `0x0000000140C234A4`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C80`
- 디코드: `29`개 명령, `127/127` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00C234C9` → [HalpBlkAllocateShadowCodePages](HalpBlkAllocateShadowCodePages_function_00C2352C.md) (function, `0x00C2352C`)
- `0x00C234EF` → [HalpBlkAddVirtualMapping](HalpBlkAddVirtualMapping_function_00C231D0.md) (function, `0x00C231D0`)
- `0x00C23517` → [HalpBlkAllocateShadowCodePages](HalpBlkAllocateShadowCodePages_function_00C2352C.md) (function, `0x00C2352C`)

### Direct callers
- [HalpBlkInitializeVirtualAddressSpace](HalpBlkInitializeVirtualAddressSpace_function_00C2368C.md) at `0x00C236A1`

### Static image references
- `0x00C234B0` → RVA `0x006AC820` (`HalpLMStub`; read)
- `0x00C234B7` → RVA `0x006ACAB4` (`HalpLMStubEnd`; read)
- `0x00C234DD` → RVA `0x00F90548` (`.data`; read)
- `0x00C234F8` → RVA `0x00E10230` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C234A4  40 53                           push rbx
00C234A6  48 83 EC 30                     sub rsp, 0x30
00C234AA  48 83 64 24 40 00               and qword ptr [rsp + 0x40], 0
00C234B0  48 8D 1D 69 93 A8 FF            lea rbx, [rip - 0x576c97]
00C234B7  48 8D 15 F6 95 A8 FF            lea rdx, [rip - 0x576a0a]
00C234BE  48 8B CB                        mov rcx, rbx
00C234C1  48 2B D3                        sub rdx, rbx
00C234C4  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
00C234C9  E8 5E 00 00 00                  call 0x140c2352c
00C234CE  85 C0                           test eax, eax
00C234D0  78 4A                           js 0x140c2351c
00C234D2  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00C234D7  41 B9 01 00 00 00               mov r9d, 1
00C234DD  48 8B 0D 64 D0 36 00            mov rcx, qword ptr [rip + 0x36d064]
00C234E4  4C 8B C3                        mov r8, rbx
00C234E7  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
00C234EF  E8 DC FC FF FF                  call 0x140c231d0
00C234F4  85 C0                           test eax, eax
00C234F6  78 24                           js 0x140c2351c
00C234F8  48 8B 05 31 CD 1E 00            mov rax, qword ptr [rip + 0x1ecd31]
00C234FF  45 33 C0                        xor r8d, r8d
00C23502  48 8B 90 F0 00 00 00            mov rdx, qword ptr [rax + 0xf0]
00C23509  48 8B 8A B0 0D 00 00            mov rcx, qword ptr [rdx + 0xdb0]
00C23510  48 8B 92 B8 0D 00 00            mov rdx, qword ptr [rdx + 0xdb8]
00C23517  E8 10 00 00 00                  call 0x140c2352c
00C2351C  48 83 C4 30                     add rsp, 0x30
00C23520  5B                              pop rbx
00C23521  C3                              ret
00C23522  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpBlkAllocateShadowCode(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (48);
    a2 = (v_rip - 5728778) - (v_rip - 5729431);
    result = HalpBlkAllocateShadowCodePages(v_rip - 5729431, a2, v_stack_p8, a4);
    if (sign_flag) goto loc_00C2351C;
    v_stack_m18 = 32;
    result = HalpBlkAddVirtualMapping(*(unsigned __int64 *)(v_rip + 3592292), v_stack_p8, v_rip - 5729431, 1);
    if (!(sign_flag)) {
        result = *(unsigned __int64 *)(v_rip + 2018609);
        a3 = 0;
        a2 = *(unsigned __int64 *)(result + 240);
        a1 = *(unsigned __int64 *)(a2 + 3504);
        a2 = *(unsigned __int64 *)(a2 + 3512);
        result = HalpBlkAllocateShadowCodePages(a1, a2, a3, 1);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpBlkAllocateShadowCode(void)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (48);
    a2 = (v_rip - 5728778) - (v_rip - 5729431);
    result = HalpBlkAllocateShadowCodePages(v_rip - 5729431, a2, v_stack_p8, a4);
    if (sign_flag) goto loc_00C2351C;
    v_stack_m18 = 32;
    result = HalpBlkAddVirtualMapping(*(uint64_t *)(v_rip + 0x36D064), v_stack_p8, v_rip - 5729431, 1);
    if (!(sign_flag)) {
        result = *(uint64_t *)(v_rip + 0x1ECD31);
        a3 = 0;
        a2 = *(uint64_t *)(result + 0xF0);
        a1 = *(uint64_t *)(a2 + 0xDB0);
        a2 = *(uint64_t *)(a2 + 0xDB8);
        result = HalpBlkAllocateShadowCodePages(a1, a2, a3, 1);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C234A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C234A4[BB_00C234A4]
  bb_00C234D2[BB_00C234D2]
  bb_00C234F8[BB_00C234F8]
  bb_00C2351C[BB_00C2351C]
  bb_00C23522[BB_00C23522]
  bb_00C234A4 -->|branch| bb_00C2351C
  bb_00C234A4 -->|fallthrough| bb_00C234D2
  bb_00C234D2 -->|branch| bb_00C2351C
  bb_00C234D2 -->|fallthrough| bb_00C234F8
  bb_00C234F8 -->|flow| bb_00C2351C
```
