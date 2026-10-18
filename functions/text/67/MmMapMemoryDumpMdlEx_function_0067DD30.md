# MmMapMemoryDumpMdlEx

- RVA: `0x0067DD30`–`0x0067DD51` (길이 `33` bytes)
- VA: `0x000000014067DD30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0067DD44` → [MiMapMemoryDumpMdl](../4A/MiMapMemoryDumpMdl_function_004A619C.md) (function, `0x004A619C`)

### Direct callers
- [IopLiveDumpBufferDumpData](../59/IopLiveDumpBufferDumpData_function_0059A938.md) at `0x0059AA9B`
- [PopCreateDumpMdl](../../pagelk/B6/PopCreateDumpMdl_function_00B6CF5C.md) at `0x00B6CFFF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0067DD30  48 83 EC 28                     sub rsp, 0x28
0067DD34  41 F7 C1 FD FF FF FF            test r9d, 0xfffffffd
0067DD3B  74 07                           je 0x14067dd44
0067DD3D  B8 F2 00 00 C0                  mov eax, 0xc00000f2
0067DD42  EB 07                           jmp 0x14067dd4b
0067DD44  E8 53 84 E2 FF                  call 0x1404a619c
0067DD49  33 C0                           xor eax, eax
0067DD4B  48 83 C4 28                     add rsp, 0x28
0067DD4F  C3                              ret
0067DD50  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmMapMemoryDumpMdlEx(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((a4) & (0xFFFFFFFDULL)) == 0) goto loc_0067DD44;
    goto loc_0067DD4B;
loc_0067DD44:
    result = MiMapMemoryDumpMdl(a1, a2, a3, a4);
    result = 0;
loc_0067DD4B:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmMapMemoryDumpMdlEx(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((Arg4) & (0xFFFFFFFDULL)) == 0) goto loc_0067DD44;
    goto loc_0067DD4B;
loc_0067DD44:
    result = MiMapMemoryDumpMdl(Arg1, Arg2, Arg3, Arg4);
    result = 0;
loc_0067DD4B:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0067DD30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0067DD30[BB_0067DD30]
  bb_0067DD3D[BB_0067DD3D]
  bb_0067DD44[BB_0067DD44]
  bb_0067DD4B[BB_0067DD4B]
  bb_0067DD50[BB_0067DD50]
  bb_0067DD30 -->|branch| bb_0067DD44
  bb_0067DD30 -->|fallthrough| bb_0067DD3D
  bb_0067DD3D -->|branch| bb_0067DD4B
  bb_0067DD44 -->|flow| bb_0067DD4B
```
