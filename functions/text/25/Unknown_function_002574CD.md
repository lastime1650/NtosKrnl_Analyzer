# sub_002574CD

- RVA: `0x002574CD`–`0x002574E0` (길이 `19` bytes)
- VA: `0x00000001402574CD`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063A00`
- 디코드: `4`개 명령, `19/19` bytes 표시
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
- `0x002574CF` → RVA `0x00FC6DBC` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002574D5` → [sub_002573C9](Unknown_function_002573C9.md) (`tail-transfer`)
  - `0x002574DB` → [sub_002573C9 + 0x11](Unknown_function_002573C9.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002574CD  2B C1                           sub eax, ecx
002574CF  3B 05 E7 F8 D6 00               cmp eax, dword ptr [rip + 0xd6f8e7]
002574D5  0F 82 EE FE FF FF               jb 0x1402573c9
002574DB  E9 FA FE FF FF                  jmp 0x1402573da
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002574CD(int a1)
{
    __int64 result;

    result = (unsigned int)((result) - (a1));
}
```

## 5. (Beta) C Style

```c
int64_t sub_002574CD(int32_t Arg1)
{
    int64_t result;

    result = (uint32_t)((result) - (Arg1));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002574CD&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002574CD[BB_002574CD]
  bb_002574DB[BB_002574DB]
  bb_002574CD -->|fallthrough| bb_002574DB
```
