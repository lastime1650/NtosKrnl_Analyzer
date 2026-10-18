# PopIsPlatformAoAcCapableInitialized

- RVA: `0x004970F4`–`0x00497101` (길이 `13` bytes)
- VA: `0x00000001404970F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `13/13` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopPdcRegister](../../page/70/PopPdcRegister_function_00704AD0.md) at `0x00704C82`

### Static image references
- `0x004970F4` → RVA `0x00E673A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004970F4  8B 05 A6 02 9D 00               mov eax, dword ptr [rip + 0x9d02a6]
004970FA  85 C0                           test eax, eax
004970FC  0F 95 C0                        setne al
004970FF  C3                              ret
00497100  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopIsPlatformAoAcCapableInitialized(void)
{
    __int64 result;

    result = ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10289830))) != 0) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
void PopIsPlatformAoAcCapableInitialized(void)
{
    int64_t result;

    result = ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9D02A6))) != 0) ? 1 : 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004970F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004970F4[BB_004970F4]
  bb_00497100[BB_00497100]
```
