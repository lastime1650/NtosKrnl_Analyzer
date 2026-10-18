# sub_003A38A5

- RVA: `0x003A38A5`–`0x003A38CA` (길이 `37` bytes)
- VA: `0x00000001403A38A5`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082240`
- 디코드: `7`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003A38B8` → [sub_006E6412 + 0x18](../6E/Unknown_function_006E6412.md) (`tail-transfer`)
  - `0x003A38C5` → [sub_006E6412](../6E/Unknown_function_006E6412.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003A38A5  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003A38AE  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
003A38B5  4D 85 C0                        test r8, r8
003A38B8  0F 84 6C 2B 34 00               je 0x1406e642a
003A38BE  41 0F 0D 08                     prefetchw byte ptr [r8]
003A38C2  41 8B 00                        mov eax, dword ptr [r8]
003A38C5  E9 48 2B 34 00                  jmp 0x1406e6412
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003A38A5(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_003A38A5(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A38A5&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003A38A5[BB_003A38A5]
  bb_003A38BE[BB_003A38BE]
  bb_003A38A5 -->|fallthrough| bb_003A38BE
```
