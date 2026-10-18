# MmAllocateDumpHibernateResources

- RVA: `0x00AB3B4C`–`0x00AB3B9D` (길이 `81` bytes)
- VA: `0x0000000140AB3B4C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005FA94`
- 디코드: `21`개 명령, `81/81` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AB3B6C` → [MiReservePtes](../../text/31/MiReservePtes_function_00318D20.md) (function, `0x00318D20`)

### Direct callers
- [IopLiveDumpAllocateMappingResources](../../text/59/IopLiveDumpAllocateMappingResources_function_0059A868.md) at `0x0059A8FE`
- [PopHiberInitializeResources](../75/PopHiberInitializeResources_function_0075D5FC.md) at `0x0075D7AF`
- [PopEnableHiberFile](../90/PopEnableHiberFile_function_0090F850.md) at `0x0090FBBB`

### Static image references
- `0x00AB3B65` → RVA `0x00E37668` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AB3B6C` → [MiReservePtes](../../text/31/MiReservePtes_function_00318D20.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB3B4C  48 83 EC 28                     sub rsp, 0x28
00AB3B50  48 F7 C1 FF 0F 00 00            test rcx, 0xfff
00AB3B57  BA 00 00 00 00                  mov edx, 0
00AB3B5C  0F 95 C2                        setne dl
00AB3B5F  48 C1 E9 0C                     shr rcx, 0xc
00AB3B63  03 D1                           add edx, ecx
00AB3B65  48 8D 0D FC 3A 38 00            lea rcx, [rip + 0x383afc]
00AB3B6C  E8 AF 51 86 FF                  call 0x140318d20
00AB3B71  48 8B C8                        mov rcx, rax
00AB3B74  48 85 C0                        test rax, rax
00AB3B77  75 06                           jne 0x140ab3b7f
00AB3B79  48 83 C4 28                     add rsp, 0x28
00AB3B7D  C3                              ret
00AB3B7E  CC                              int3
00AB3B7F  48 C1 E1 19                     shl rcx, 0x19
00AB3B83  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00AB3B8D  48 C1 E0 19                     shl rax, 0x19
00AB3B91  48 2B C8                        sub rcx, rax
00AB3B94  48 C1 F9 10                     sar rcx, 0x10
00AB3B98  48 8B C1                        mov rax, rcx
00AB3B9B  EB DC                           jmp 0x140ab3b79
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmAllocateDumpHibernateResources(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = (((a1) & (0xFFFULL)) != 0) ? 1 : 0;
    a1 = (a1) >> (12);
    a2 = (unsigned int)((a2) + ((unsigned int)(a1)));
    result = MiReservePtes(v_rip + 3685116, a2, a3, a4);
    if (result != 0) goto loc_00AB3B7F;
loc_00AB3B79:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00AB3B7F:
    a1 = (result) << (25);
    result = (result) << (25);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    goto loc_00AB3B79;
}
```

## 5. (Beta) C Style

```c
int64_t MmAllocateDumpHibernateResources(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    a2 = (((Arg1) & (0xFFFULL)) != 0) ? 1 : 0;
    Arg1 = (Arg1) >> (12);
    a2 = (uint32_t)((a2) + ((uint32_t)(Arg1)));
    result = MiReservePtes(v_rip + 3685116, a2, a3, a4);
    if (result != 0) goto loc_00AB3B7F;
loc_00AB3B79:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00AB3B7F:
    Arg1 = (result) << (25);
    result = (result) << (25);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    goto loc_00AB3B79;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB3B4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB3B4C[BB_00AB3B4C]
  bb_00AB3B79[BB_00AB3B79]
  bb_00AB3B7E[BB_00AB3B7E]
  bb_00AB3B7F[BB_00AB3B7F]
  bb_00AB3B4C -->|branch| bb_00AB3B7F
  bb_00AB3B4C -->|fallthrough| bb_00AB3B79
  bb_00AB3B7E -->|flow| bb_00AB3B7F
  bb_00AB3B7F -->|branch| bb_00AB3B79
```
