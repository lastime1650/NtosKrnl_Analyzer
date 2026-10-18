# sub_009A6C56

- RVA: `0x009A6C56`–`0x009A6C71` (길이 `27` bytes)
- VA: `0x00000001409A6C56`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009C914`
- 디코드: `5`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009A6C67` → [RtlCopyXStateArea](../../text/3D/RtlCopyXStateArea_function_003D5850.md) (function, `0x003D5850`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009A6C67` → [RtlCopyXStateArea](../../text/3D/RtlCopyXStateArea_function_003D5850.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x009A6C6C` → [sub_009A6B68 + 0x4A](Unknown_function_009A6B68.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009A6C56  48 A1 D8 03 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff780000003d8]
009A6C60  48 83 E0 FC                     and rax, 0xfffffffffffffffc
009A6C64  48 8B D0                        mov rdx, rax
009A6C67  E8 E4 EB A2 FF                  call 0x1403d5850
009A6C6C  E9 41 FF FF FF                  jmp 0x1409a6bb2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009A6C56(void)
{
    __int64 result;

    result = (result) & (-4);
    result = RtlCopyXStateArea(a1, result, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_009A6C56(void)
{
    int64_t result;

    result = (result) & (-4);
    result = RtlCopyXStateArea(a1, result, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A6C56&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A6C56[BB_009A6C56]
```
