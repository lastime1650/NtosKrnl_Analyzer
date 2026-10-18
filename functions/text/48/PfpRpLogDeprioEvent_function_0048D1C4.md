# PfpRpLogDeprioEvent

- RVA: `0x0048D1C4`–`0x0048D252` (길이 `142` bytes)
- VA: `0x000000014048D1C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B13B4`
- 디코드: `34`개 명령, `142/142` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0048D240` → [PfLogEvent](../34/PfLogEvent_function_00349BA8.md) (function, `0x00349BA8`)

### Direct callers
- [PfCheckDeprioritizeFile](../../page/88/PfCheckDeprioritizeFile_function_00887F6C.md) at `0x0088804D`

### Static image references
- `0x0048D1E2` → RVA `0x00F0F228` (`.data`; read)
- `0x0048D239` → RVA `0x00E670CC` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048D1C4  4C 8B DC                        mov r11, rsp
0048D1C7  48 83 EC 58                     sub rsp, 0x58
0048D1CB  4C 8B D1                        mov r10, rcx
0048D1CE  48 85 C9                        test rcx, rcx
0048D1D1  74 78                           je 0x14048d24b
0048D1D3  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
0048D1D8  48 B9 04 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000004
0048D1E2  8B 05 40 20 A8 00               mov eax, dword ptr [rip + 0xa82040]
0048D1E8  49 89 53 D8                     mov qword ptr [r11 - 0x28], rdx
0048D1EC  BA 1E 00 00 00                  mov edx, 0x1e
0048D1F1  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0048D1F5  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0048D1FF  45 89 43 E4                     mov dword ptr [r11 - 0x1c], r8d
0048D203  45 89 4B E8                     mov dword ptr [r11 - 0x18], r9d
0048D207  4D 8D 4B D8                     lea r9, [r11 - 0x28]
0048D20B  C7 44 24 20 18 00 00 00         mov dword ptr [rsp + 0x20], 0x18
0048D213  48 8B 00                        mov rax, qword ptr [rax]
0048D216  8B 09                           mov ecx, dword ptr [rcx]
0048D218  44 8B C0                        mov r8d, eax
0048D21B  4C 0F AF C1                     imul r8, rcx
0048D21F  48 C1 E8 20                     shr rax, 0x20
0048D223  49 C1 E8 18                     shr r8, 0x18
0048D227  48 0F AF C1                     imul rax, rcx
0048D22B  49 8B CA                        mov rcx, r10
0048D22E  48 C1 E0 08                     shl rax, 8
0048D232  4C 03 C0                        add r8, rax
0048D235  49 C1 E8 0A                     shr r8, 0xa
0048D239  44 03 05 8C 9E 9D 00            add r8d, dword ptr [rip + 0x9d9e8c]
0048D240  E8 63 C9 EB FF                  call 0x140349ba8
0048D245  48 83 C4 58                     add rsp, 0x58
0048D249  C3                              ret
0048D24A  CC                              int3
0048D24B  B8 89 01 00 C0                  mov eax, 0xc0000189
0048D250  EB F3                           jmp 0x14048d245
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfpRpLogDeprioEvent(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m14;
    unsigned int v_stack_m20;
    unsigned int v_stack_m38;

    v_rsp = (v_rsp) - (88);
    if (a1 == 0) goto loc_0048D24B;
    *(unsigned __int64 *)(v_rsp - 40) = a2;
    v_stack_m20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11018304)));
    *(unsigned int *)(v_rsp - 28) = a3;
    *(unsigned int *)(v_rsp - 24) = a4;
    v_stack_m38 = 24;
    a3 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rip + 11018304)))))) * ((unsigned int)(*(unsigned int *)(a1)));
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rip + 11018304)))) >> (32);
    a3 = (a3) >> (24);
    result = (result) * ((unsigned int)(*(unsigned int *)(a1)));
    result = (result) << (8);
    a3 = (a3) + (result);
    a3 = (a3) >> (10);
    a3 = (unsigned int)((a3) + (*(unsigned int *)(v_rip + 10329740)));
    result = PfLogEvent(a1, 30, a3, v_rsp - 40);
loc_0048D245:
    v_rsp = (v_rsp) + (88);
    return result;
loc_0048D24B:
    goto loc_0048D245;
}
```

## 5. (Beta) C Style

```c
int64_t PfpRpLogDeprioEvent(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m14;
    uint32_t v_stack_m20;
    uint32_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    if (Arg1 == 0) goto loc_0048D24B;
    *(uint64_t *)(local_rsp - 0x28) = Arg2;
    v_stack_m20 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA82040)));
    *(uint32_t *)(local_rsp - 0x1C) = Arg3;
    *(uint32_t *)(local_rsp - 0x18) = Arg4;
    v_stack_m38 = 24;
    Arg3 = ((uint32_t)((uint32_t)(*(uint64_t *)((uint32_t)(*(uint32_t *)(v_rip + 0xA82040)))))) * ((uint32_t)(*(uint32_t *)(Arg1)));
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_rip + 0xA82040)))) >> (32);
    Arg3 = (Arg3) >> (24);
    result = (result) * ((uint32_t)(*(uint32_t *)(Arg1)));
    result = (result) << (8);
    Arg3 = (Arg3) + (result);
    Arg3 = (Arg3) >> (10);
    Arg3 = (uint32_t)((Arg3) + (*(uint32_t *)(v_rip + 0x9D9E8C)));
    result = PfLogEvent(Arg1, 30, Arg3, local_rsp - 40);
loc_0048D245:
    local_rsp = (local_rsp) + (88);
    return result;
loc_0048D24B:
    goto loc_0048D245;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048D1C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048D1C4[BB_0048D1C4]
  bb_0048D1D3[BB_0048D1D3]
  bb_0048D245[BB_0048D245]
  bb_0048D24A[BB_0048D24A]
  bb_0048D24B[BB_0048D24B]
  bb_0048D1C4 -->|branch| bb_0048D24B
  bb_0048D1C4 -->|fallthrough| bb_0048D1D3
  bb_0048D1D3 -->|flow| bb_0048D245
  bb_0048D24A -->|flow| bb_0048D24B
  bb_0048D24B -->|branch| bb_0048D245
```
