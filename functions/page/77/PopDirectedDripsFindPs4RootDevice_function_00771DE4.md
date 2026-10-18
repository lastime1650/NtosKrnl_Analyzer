# PopDirectedDripsFindPs4RootDevice

- RVA: `0x00771DE4`–`0x00771DFE` (길이 `26` bytes)
- VA: `0x0000000140771DE4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopDirectedDripsBuildPs4BroadcastTree](PopDirectedDripsBuildPs4BroadcastTree_function_00771C90.md) at `0x00771D13`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00771DE4  EB 0E                           jmp 0x140771df4
00771DE6  8B 81 F8 02 00 00               mov eax, dword ptr [rcx + 0x2f8]
00771DEC  A8 01                           test al, 1
00771DEE  75 09                           jne 0x140771df9
00771DF0  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00771DF4  48 85 C9                        test rcx, rcx
00771DF7  75 ED                           jne 0x140771de6
00771DF9  48 8B C1                        mov rax, rcx
00771DFC  C3                              ret
00771DFD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDirectedDripsFindPs4RootDevice(__int64 a1)
{
    goto loc_00771DF4;
loc_00771DE6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 760)))) & (1)) != 0) goto loc_00771DF9;
loc_00771DF4:
    if (*(unsigned __int64 *)(a1 + 16) != 0) goto loc_00771DE6;
loc_00771DF9:
    return *(unsigned __int64 *)(a1 + 16);
}
```

## 5. (Beta) C Style

```c
int64_t PopDirectedDripsFindPs4RootDevice(int64_t Arg1)
{
    goto loc_00771DF4;
loc_00771DE6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x2F8)))) & (1)) != 0) goto loc_00771DF9;
loc_00771DF4:
    if (*(uint64_t *)(Arg1 + 0x10) != 0) goto loc_00771DE6;
loc_00771DF9:
    return *(uint64_t *)(Arg1 + 0x10);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00771DE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00771DE4[BB_00771DE4]
  bb_00771DE6[BB_00771DE6]
  bb_00771DF0[BB_00771DF0]
  bb_00771DF4[BB_00771DF4]
  bb_00771DF9[BB_00771DF9]
  bb_00771DFD[BB_00771DFD]
  bb_00771DE4 -->|branch| bb_00771DF4
  bb_00771DE6 -->|branch| bb_00771DF9
  bb_00771DE6 -->|fallthrough| bb_00771DF0
  bb_00771DF0 -->|flow| bb_00771DF4
  bb_00771DF4 -->|branch| bb_00771DE6
  bb_00771DF4 -->|fallthrough| bb_00771DF9
```
