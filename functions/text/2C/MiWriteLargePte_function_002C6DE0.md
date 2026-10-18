# MiWriteLargePte

- RVA: `0x002C6DE0`–`0x002C6E1D` (길이 `61` bytes)
- VA: `0x00000001402C6DE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006ECB4`
- 디코드: `16`개 명령, `61/61` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiZeroLargePage](MiZeroLargePage_function_002C6914.md) at `0x002C6BE2`
- [MiZeroLargePage](MiZeroLargePage_function_002C6914.md) at `0x002C6C07`
- [MiZeroWithUltraSpace](MiZeroWithUltraSpace_function_002C6C9C.md) at `0x002C6D5F`
- [MiZeroWithUltraSpace](MiZeroWithUltraSpace_function_002C6C9C.md) at `0x002C6D84`
- [MiMapWithLargePages](../3B/MiMapWithLargePages_function_003B6624.md) at `0x003B68C5`
- [MiInsertLargeUserMapping](../3D/MiInsertLargeUserMapping_function_003D3154.md) at `0x003D32D1`
- [MiInitializeNewUltraHugeContext](../3F/MiInitializeNewUltraHugeContext_function_003FB974.md) at `0x003FBBE1`
- [MiMapMdlWithLargePages](../4D/MiMapMdlWithLargePages_function_004D10B8.md) at `0x004D1452`
- [MiHugePageOperation](../68/MiHugePageOperation_function_0068C490.md) at `0x0068C5A3`
- [MiHugePageOperation](../68/MiHugePageOperation_function_0068C490.md) at `0x0068C630`
- [MiReleaseProcessorHugeMappingAtDpc](../68/MiReleaseProcessorHugeMappingAtDpc_function_0068C68C.md) at `0x0068C6B0`
- [MiUseProcessorHugeMappingAtDpc](../68/MiUseProcessorHugeMappingAtDpc_function_0068C894.md) at `0x0068C92D`
- [MiScrubLargePage](../69/MiScrubLargePage_function_006942E8.md) at `0x0069457C`
- [MxMapVa](../../init/C6/MxMapVa_function_00C63EC4.md) at `0x00C64028`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002C6E17` → [sub_002C7127](Unknown_function_002C7127.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002C6DE0  40 55                           push rbp
002C6DE2  56                              push rsi
002C6DE3  57                              push rdi
002C6DE4  41 54                           push r12
002C6DE6  48 83 EC 28                     sub rsp, 0x28
002C6DEA  48 8B F9                        mov rdi, rcx
002C6DED  41 8B E8                        mov ebp, r8d
002C6DF0  48 C1 EF 09                     shr rdi, 9
002C6DF4  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
002C6DFE  49 23 F8                        and rdi, r8
002C6E01  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
002C6E0B  41 8B F1                        mov esi, r9d
002C6E0E  49 8B C4                        mov rax, r12
002C6E11  48 03 F8                        add rdi, rax
002C6E14  83 FD 01                        cmp ebp, 1
002C6E17  0F 86 0A 03 00 00               jbe 0x1402c7127
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiWriteLargePte(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 v_rdi;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    v_rdi = (a1) >> (9);
    v_rdi = (v_rdi) & (a3);
    v_rdi = (v_rdi) + (v_r12);
}
```

## 5. (Beta) C Style

```c
int64_t MiWriteLargePte(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t local_rdi;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    local_rdi = (Arg1) >> (9);
    local_rdi = (local_rdi) & (Arg3);
    local_rdi = (local_rdi) + (local_r12);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C6DE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C6DE0[BB_002C6DE0]
```
