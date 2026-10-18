# HalpWheaReadMsrMisc

- RVA: `0x004872EC`–`0x0048732F` (길이 `67` bytes)
- VA: `0x00000001404872EC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A618`
- 디코드: `18`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004872F3` → [HalpGetCpuVendor](HalpGetCpuVendor_function_004879E4.md) (function, `0x004879E4`)
- `0x00487310` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpCmciSetProcessorConfigAMD](HalpCmciSetProcessorConfigAMD_function_00487BE0.md) at `0x00487CAE`
- [HalpMcaPopulateErrorData](../54/HalpMcaPopulateErrorData_function_005417AC.md) at `0x005418A2`
- [HalpMcaPopulateErrorDataEx](../54/HalpMcaPopulateErrorDataEx_function_0054198C.md) at `0x005419FD`
- [HalpIsCmciImplementedAMD](../../pagelk/B5/HalpIsCmciImplementedAMD_function_00B5C37C.md) at `0x00B5C3DE`

### Static image references
- `0x00487303` → RVA `0x00FC1990` (`.data`; read)
- `0x0048731B` → RVA `0x00E10258` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004872EC  48 83 EC 28                     sub rsp, 0x28
004872F0  4C 8B C9                        mov r9, rcx
004872F3  E8 EC 06 00 00                  call 0x1404879e4
004872F8  3C 01                           cmp al, 1
004872FA  74 1F                           je 0x14048731b
004872FC  8D 14 95 03 04 00 00            lea edx, [rdx*4 + 0x403]
00487303  48 8B 05 86 A6 B3 00            mov rax, qword ptr [rip + 0xb3a686]
0048730A  45 33 C0                        xor r8d, r8d
0048730D  49 8B C9                        mov rcx, r9
00487310  E8 BB 37 23 00                  call 0x1406baad0
00487315  48 83 C4 28                     add rsp, 0x28
00487319  C3                              ret
0048731A  CC                              int3
0048731B  80 3D 36 8F 98 00 00            cmp byte ptr [rip + 0x988f36], 0
00487322  74 D8                           je 0x1404872fc
00487324  C1 E2 04                        shl edx, 4
00487327  81 EA FD DF FF 3F               sub edx, 0x3fffdffd
0048732D  EB D4                           jmp 0x140487303
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpWheaReadMsrMisc(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = HalpGetCpuVendor(a1, a2, a3, a1);
    if (((unsigned __int8)(result)) == 1) goto loc_0048731B;
loc_004872FC:
loc_00487303:
    a3 = 0;
    result = guard_dispatch_icall(a1, a2 * 4 + 1027, a3, a1);
    v_rsp = (v_rsp) + (40);
    return result;
loc_0048731B:
    if ((*(unsigned __int8 *)(v_rip + 9998134)) == 0) goto loc_004872FC;
    a2 = (unsigned int)((a2 * 4 + 1027) << (4));
    a2 = (unsigned int)((a2) - (0x3FFFDFFDULL));
    goto loc_00487303;
}
```

## 5. (Beta) C Style

```c
int64_t HalpWheaReadMsrMisc(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = HalpGetCpuVendor(Arg1, Arg2, Arg3, Arg1);
    if (((uint8_t)(result)) == 1) goto loc_0048731B;
loc_004872FC:
loc_00487303:
    Arg3 = 0;
    result = guard_dispatch_icall(Arg1, Arg2 * 4 + 1027, Arg3, Arg1);
    local_rsp = (local_rsp) + (40);
    return result;
loc_0048731B:
    if ((*(uint8_t *)(v_rip + 0x988F36)) == 0) goto loc_004872FC;
    Arg2 = (uint32_t)((Arg2 * 4 + 1027) << (4));
    Arg2 = (uint32_t)((Arg2) - (0x3FFFDFFDULL));
    goto loc_00487303;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004872EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004872EC[BB_004872EC]
  bb_004872FC[BB_004872FC]
  bb_00487303[BB_00487303]
  bb_0048731A[BB_0048731A]
  bb_0048731B[BB_0048731B]
  bb_00487324[BB_00487324]
  bb_004872EC -->|branch| bb_0048731B
  bb_004872EC -->|fallthrough| bb_004872FC
  bb_004872FC -->|flow| bb_00487303
  bb_0048731A -->|flow| bb_0048731B
  bb_0048731B -->|branch| bb_004872FC
  bb_0048731B -->|fallthrough| bb_00487324
  bb_00487324 -->|branch| bb_00487303
```
