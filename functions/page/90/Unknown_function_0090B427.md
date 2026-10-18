# sub_0090B427

- RVA: `0x0090B427`–`0x0090B43E` (길이 `23` bytes)
- VA: `0x000000014090B427`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00089160`
- 디코드: `5`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0090B434` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0090B434` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0090B42E` → [ExpWnfResolveScopeInstance + 0x4A](ExpWnfResolveScopeInstance_function_0090B280.md) (`tail-transfer`)
  - `0x0090B439` → [ExpWnfResolveScopeInstance + 0x57](ExpWnfResolveScopeInstance_function_0090B280.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0090B427  41 8D 47 FC                     lea eax, [r15 - 4]
0090B42B  83 F8 01                        cmp eax, 1
0090B42E  0F 86 96 FE FF FF               jbe 0x14090b2ca
0090B434  E8 B7 2D 9F FF                  call 0x1402fe1f0
0090B439  E9 99 FE FF FF                  jmp 0x14090b2d7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0090B427(void)
{
    __int64 result;

    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0090B427(void)
{
    int64_t result;

    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0090B427&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0090B427[BB_0090B427]
  bb_0090B434[BB_0090B434]
  bb_0090B427 -->|fallthrough| bb_0090B434
```
