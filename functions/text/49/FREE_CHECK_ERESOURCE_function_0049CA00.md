# FREE_CHECK_ERESOURCE

- RVA: `0x0049CA00`–`0x0049CA1D` (길이 `29` bytes)
- VA: `0x000000014049CA00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `10`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0049CA0E` → [ExpCheckForResource](ExpCheckForResource_function_0049CA24.md) (function, `0x0049CA24`)

### Direct callers
- [ExAllocateHeapPool](../35/ExAllocateHeapPool_function_0035BA30.md) at `0x0035E669`

### Static image references
- `0x0049CA04` → RVA `0x00FC6BD0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0049CA00  48 83 EC 28                     sub rsp, 0x28
0049CA04  8B 05 C6 A1 B2 00               mov eax, dword ptr [rip + 0xb2a1c6]
0049CA0A  A8 04                           test al, 4
0049CA0C  74 0B                           je 0x14049ca19
0049CA0E  E8 11 00 00 00                  call 0x14049ca24
0049CA13  48 83 C4 28                     add rsp, 0x28
0049CA17  C3                              ret
0049CA18  CC                              int3
0049CA19  33 C0                           xor eax, eax
0049CA1B  EB F6                           jmp 0x14049ca13
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FREE_CHECK_ERESOURCE(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11706822)))) & (4)) == 0) goto loc_0049CA19;
    result = ExpCheckForResource(a1, a2, a3, a4);
loc_0049CA13:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0049CA19:
    result = 0;
    goto loc_0049CA13;
}
```

## 5. (Beta) C Style

```c
void FREE_CHECK_ERESOURCE(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB2A1C6)))) & (4)) == 0) goto loc_0049CA19;
    result = ExpCheckForResource(a1, a2, a3, a4);
loc_0049CA13:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0049CA19:
    result = 0;
    goto loc_0049CA13;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0049CA00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0049CA00[BB_0049CA00]
  bb_0049CA0E[BB_0049CA0E]
  bb_0049CA13[BB_0049CA13]
  bb_0049CA18[BB_0049CA18]
  bb_0049CA19[BB_0049CA19]
  bb_0049CA00 -->|branch| bb_0049CA19
  bb_0049CA00 -->|fallthrough| bb_0049CA0E
  bb_0049CA0E -->|flow| bb_0049CA13
  bb_0049CA18 -->|flow| bb_0049CA19
  bb_0049CA19 -->|branch| bb_0049CA13
```
