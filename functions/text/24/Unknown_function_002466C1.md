# sub_002466C1

- RVA: `0x002466C1`–`0x002466D9` (길이 `24` bytes)
- VA: `0x00000001402466C1`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00062050`
- 디코드: `5`개 명령, `24/24` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002466D4` → [sub_002460E6 + 0x24](Unknown_function_002460E6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002466C1  48 8B 03                        mov rax, qword ptr [rbx]
002466C4  48 BA 01 00 00 00 00 F0 FF FF   movabs rdx, 0xfffff00000000001
002466CE  48 23 C2                        and rax, rdx
002466D1  48 89 03                        mov qword ptr [rbx], rax
002466D4  E9 31 FA FF FF                  jmp 0x14024610a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002466C1(void)
{
    __int64 result;

    result = (*(unsigned __int64 *)(v_rbx)) & (a2);
    *(unsigned __int64 *)(v_rbx) = result;
}
```

## 5. (Beta) C Style

```c
void sub_002466C1(void)
{
    int64_t result;

    result = (*(uint64_t *)(local_rbx)) & (a2);
    *(uint64_t *)(local_rbx) = result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002466C1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002466C1[BB_002466C1]
```
