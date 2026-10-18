# sub_003FAD78

- RVA: `0x003FAD78`–`0x003FAD8F` (길이 `23` bytes)
- VA: `0x00000001403FAD78`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009852C`
- 디코드: `6`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003FAD88` → [KiBeginCounterAccumulation](../49/KiBeginCounterAccumulation_function_0049D3F0.md) (function, `0x0049D3F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003FAD7E` → [sub_003FAC55 + 0x59](Unknown_function_003FAC55.md) (`tail-transfer`)
  - `0x003FAD8D` → [sub_003FAC55 + 0xBB](Unknown_function_003FAC55.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003FAD78  41 B8 64 00 00 00               mov r8d, 0x64
003FAD7E  E9 2B FF FF FF                  jmp 0x1403facae
003FAD83  33 D2                           xor edx, edx
003FAD85  49 8B CA                        mov rcx, r10
003FAD88  E8 63 26 0A 00                  call 0x14049d3f0
003FAD8D  EB 81                           jmp 0x1403fad10
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003FAD78(__int64 a1, int a2)
{
}
```

## 5. (Beta) C Style

```c
int64_t sub_003FAD78(int64_t Arg1, int32_t Arg2)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FAD78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003FAD78[BB_003FAD78]
  bb_003FAD83[BB_003FAD83]
```
