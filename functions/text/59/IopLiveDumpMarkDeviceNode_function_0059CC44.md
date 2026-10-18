# IopLiveDumpMarkDeviceNode

- RVA: `0x0059CC44`–`0x0059CC9D` (길이 `89` bytes)
- VA: `0x000000014059CC44`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `26`개 명령, `89/89` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0059CC5A` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x0059CC73` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)
- `0x0059CC8C` → [MmAddRangeToCrashDump](../67/MmAddRangeToCrashDump_function_0067D8B0.md) (function, `0x0067D8B0`)

### Direct callers
- [IopLiveDumpMarkRequiredDumpData](IopLiveDumpMarkRequiredDumpData_function_0059D070.md) at `0x0059D1FA`
- [IopLiveDumpMarkRequiredDumpData](IopLiveDumpMarkRequiredDumpData_function_0059D070.md) at `0x0059D212`
- [IopAddLiveDumpPagesToPartialKernelDump](../5A/IopAddLiveDumpPagesToPartialKernelDump_function_005A13AC.md) at `0x005A15B5`
- [IopAddLiveDumpPagesToPartialKernelDump](../5A/IopAddLiveDumpPagesToPartialKernelDump_function_005A13AC.md) at `0x005A15CF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0059CC44  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0059CC49  57                              push rdi
0059CC4A  48 83 EC 20                     sub rsp, 0x20
0059CC4E  41 B8 58 00 00 00               mov r8d, 0x58
0059CC54  48 8B DA                        mov rbx, rdx
0059CC57  48 8B F9                        mov rdi, rcx
0059CC5A  E8 51 0C 0E 00                  call 0x14067d8b0
0059CC5F  85 C0                           test eax, eax
0059CC61  78 2E                           js 0x14059cc91
0059CC63  44 0F B7 43 28                  movzx r8d, word ptr [rbx + 0x28]
0059CC68  48 8B CF                        mov rcx, rdi
0059CC6B  48 8B 53 30                     mov rdx, qword ptr [rbx + 0x30]
0059CC6F  49 83 C0 02                     add r8, 2
0059CC73  E8 38 0C 0E 00                  call 0x14067d8b0
0059CC78  85 C0                           test eax, eax
0059CC7A  78 15                           js 0x14059cc91
0059CC7C  44 0F B7 43 38                  movzx r8d, word ptr [rbx + 0x38]
0059CC81  48 8B CF                        mov rcx, rdi
0059CC84  48 8B 53 40                     mov rdx, qword ptr [rbx + 0x40]
0059CC88  49 83 C0 02                     add r8, 2
0059CC8C  E8 1F 0C 0E 00                  call 0x14067d8b0
0059CC91  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0059CC96  48 83 C4 20                     add rsp, 0x20
0059CC9A  5F                              pop rdi
0059CC9B  C3                              ret
0059CC9C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopLiveDumpMarkDeviceNode(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = MmAddRangeToCrashDump(a1, a2, 88, a4);
    if (sign_flag) goto loc_0059CC91;
    a3 = (*(unsigned __int16 *)(a2 + 40)) + (2);
    result = MmAddRangeToCrashDump(a1, *(unsigned __int64 *)(a2 + 48), a3, a4);
    if (!(sign_flag)) {
        a3 = *(unsigned __int16 *)(a2 + 56);
        a1 = a1;
        a2 = *(unsigned __int64 *)(a2 + 64);
        a3 = (a3) + (2);
        result = MmAddRangeToCrashDump(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopLiveDumpMarkDeviceNode(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = MmAddRangeToCrashDump(Arg1, Arg2, 88, a4);
    if (sign_flag) goto loc_0059CC91;
    a3 = (*(uint16_t *)(arg2 + 0x28)) + (2);
    result = MmAddRangeToCrashDump(Arg1, *(uint64_t *)(arg2 + 0x30), a3, a4);
    if (!(sign_flag)) {
        a3 = *(uint16_t *)(arg2 + 0x38);
        Arg1 = Arg1;
        Arg2 = *(uint64_t *)(arg2 + 0x40);
        a3 = (a3) + (2);
        result = MmAddRangeToCrashDump(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x28` | `16` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R` |
| `Arg2` | `+ 0x38` | `16` | `R` |
| `Arg2` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0059CC44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0059CC44[BB_0059CC44]
  bb_0059CC63[BB_0059CC63]
  bb_0059CC7C[BB_0059CC7C]
  bb_0059CC91[BB_0059CC91]
  bb_0059CC9C[BB_0059CC9C]
  bb_0059CC44 -->|branch| bb_0059CC91
  bb_0059CC44 -->|fallthrough| bb_0059CC63
  bb_0059CC63 -->|branch| bb_0059CC91
  bb_0059CC63 -->|fallthrough| bb_0059CC7C
  bb_0059CC7C -->|flow| bb_0059CC91
```
