# sub_0093389E

- RVA: `0x0093389E`–`0x009338BA` (길이 `28` bytes)
- VA: `0x000000014093389E`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008EFF8`
- 디코드: `6`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009338B0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009338B0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x009338A2` → [sub_0093342A](Unknown_function_0093342A.md) (`tail-transfer`)
  - `0x009338B5` → [sub_0093342A](Unknown_function_0093342A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0093389E  4C 3B 75 60                     cmp r14, qword ptr [rbp + 0x60]
009338A2  0F 84 82 FB FF FF               je 0x14093342a
009338A8  BA 56 52 65 67                  mov edx, 0x67655256
009338AD  49 8B CE                        mov rcx, r14
009338B0  E8 2B 40 9C FF                  call 0x1402f78e0
009338B5  E9 70 FB FF FF                  jmp 0x14093342a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0093389E(void)
{
    __int64 result;

    result = ObfDereferenceObjectWithTag(v_r14, (unsigned int)(0x67655256ULL), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0093389E(void)
{
    int64_t result;

    result = ObfDereferenceObjectWithTag(local_r14, (uint32_t)(0x67655256ULL), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0093389E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0093389E[BB_0093389E]
  bb_009338A8[BB_009338A8]
  bb_0093389E -->|fallthrough| bb_009338A8
```
