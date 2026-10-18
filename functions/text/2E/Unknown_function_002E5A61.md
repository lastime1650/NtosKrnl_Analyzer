# sub_002E5A61

- RVA: `0x002E5A61`–`0x002E5A72` (길이 `17` bytes)
- VA: `0x00000001402E5A61`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000711CC`
- 디코드: `6`개 명령, `17/17` bytes 표시
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
  - `0x002E5A68` → [sub_002E59C5 + 0x6A](Unknown_function_002E59C5.md) (`tail-transfer`)
  - `0x002E5A6D` → [sub_002E59C5 + 0x28](Unknown_function_002E59C5.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002E5A61  48 85 D2                        test rdx, rdx
002E5A64  75 04                           jne 0x1402e5a6a
002E5A66  32 C0                           xor al, al
002E5A68  EB C5                           jmp 0x1402e5a2f
002E5A6A  48 33 D7                        xor rdx, rdi
002E5A6D  E9 7B FF FF FF                  jmp 0x1402e59ed
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002E5A61(__int64 a1, __int64 a2)
{
    __int64 result;

    if (a2 != 0) goto loc_002E5A6A;
    result = 0;
loc_002E5A6A:
    a2 = (a2) ^ (v_rdi);
}
```

## 5. (Beta) C Style

```c
int64_t sub_002E5A61(int64_t Arg1, int64_t Arg2)
{
    int64_t result;

    if (Arg2 != 0) goto loc_002E5A6A;
    result = 0;
loc_002E5A6A:
    Arg2 = (Arg2) ^ (local_rdi);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E5A61&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002E5A61[BB_002E5A61]
  bb_002E5A66[BB_002E5A66]
  bb_002E5A6A[BB_002E5A6A]
  bb_002E5A61 -->|branch| bb_002E5A6A
  bb_002E5A61 -->|fallthrough| bb_002E5A66
```
