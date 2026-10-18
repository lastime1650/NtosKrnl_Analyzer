# sub_009E5C4D

- RVA: `0x009E5C4D`–`0x009E5C69` (길이 `28` bytes)
- VA: `0x00000001409E5C4D`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A4244`
- 디코드: `7`개 명령, `28/28` bytes 표시
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
  - `0x009E5C5E` → [sub_009E57A9](Unknown_function_009E57A9.md) (`tail-transfer`)
  - `0x009E5C64` → [sub_009E5A16 + 0x8](Unknown_function_009E5A16.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009E5C4D  8B 4E 34                        mov ecx, dword ptr [rsi + 0x34]
009E5C50  0F B6 56 22                     movzx edx, byte ptr [rsi + 0x22]
009E5C54  48 C1 E2 20                     shl rdx, 0x20
009E5C58  48 0B D1                        or rdx, rcx
009E5C5B  49 3B D0                        cmp rdx, r8
009E5C5E  0F 84 45 FB FF FF               je 0x1409e57a9
009E5C64  E9 B5 FD FF FF                  jmp 0x1409e5a1e
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_009E5C4D(__int64 a1, __int64 a2, __int64 a3)
{
    a2 = (*(unsigned __int8 *)(v_rsi + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(v_rsi + 52)));
}
```

## 5. (Beta) C Style

```c
void sub_009E5C4D(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    Arg2 = (*(uint8_t *)(local_rsi + 0x22)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(local_rsi + 0x34)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009E5C4D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009E5C4D[BB_009E5C4D]
  bb_009E5C64[BB_009E5C64]
  bb_009E5C4D -->|fallthrough| bb_009E5C64
```
