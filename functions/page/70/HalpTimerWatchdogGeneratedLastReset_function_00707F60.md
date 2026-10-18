# HalpTimerWatchdogGeneratedLastReset

- RVA: `0x00707F60`–`0x00707F7B` (길이 `27` bytes)
- VA: `0x0000000140707F60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpTimerWatchdogLogReset](HalpTimerWatchdogLogReset_function_00707F84.md) at `0x00707F88`

### Static image references
- `0x00707F60` → RVA `0x00FC4028` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00707F60  48 8B 05 C1 C0 8B 00            mov rax, qword ptr [rip + 0x8bc0c1]
00707F67  48 85 C0                        test rax, rax
00707F6A  74 0D                           je 0x140707f79
00707F6C  8B 80 E0 00 00 00               mov eax, dword ptr [rax + 0xe0]
00707F72  C1 E8 12                        shr eax, 0x12
00707F75  24 01                           and al, 1
00707F77  C3                              ret
00707F78  CC                              int3
00707F79  C3                              ret
00707F7A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpTimerWatchdogGeneratedLastReset(void)
{
    __int64 result;

    if (*(unsigned __int64 *)(v_rip + 9158849) == 0) goto loc_00707F79;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9158849) + 224))) >> (18));
    result = (unsigned __int8)((result) & (1));
    return result;
loc_00707F79:
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpTimerWatchdogGeneratedLastReset(void)
{
    int64_t result;

    if (*(uint64_t *)(v_rip + 0x8BC0C1) == 0) goto loc_00707F79;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8BC0C1) + 0xE0))) >> (18));
    result = (uint8_t)((result) & (1));
    return result;
loc_00707F79:
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00707F60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00707F60[BB_00707F60]
  bb_00707F6C[BB_00707F6C]
  bb_00707F78[BB_00707F78]
  bb_00707F79[BB_00707F79]
  bb_00707F7A[BB_00707F7A]
  bb_00707F60 -->|branch| bb_00707F79
  bb_00707F60 -->|fallthrough| bb_00707F6C
  bb_00707F78 -->|flow| bb_00707F79
```
