# NtIsUILanguageComitted

- RVA: `0x00A9F920`–`0x00A9F933` (길이 `19` bytes)
- VA: `0x0000000140A9F920`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `19/19` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00A9F920` → RVA `0x00FD9BB8` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A9F920  8B 05 92 A2 53 00               mov eax, dword ptr [rip + 0x53a292]
00A9F926  F7 D8                           neg eax
00A9F928  1B C0                           sbb eax, eax
00A9F92A  F7 D0                           not eax
00A9F92C  25 34 00 00 C0                  and eax, 0xc0000034
00A9F931  C3                              ret
00A9F932  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtIsUILanguageComitted(void)
{
    __int64 result;

    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rip + 5481106))));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (0xC0000034ULL));
    return result;
}
```

## 5. (Beta) C Style

```c
void NtIsUILanguageComitted(void)
{
    int64_t result;

    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_rip + 0x53A292))));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (0xC0000034ULL));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A9F920&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A9F920[BB_00A9F920]
  bb_00A9F932[BB_00A9F932]
```
