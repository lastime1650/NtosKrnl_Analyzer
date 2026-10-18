# sub_0042E3BB

- RVA: `0x0042E3BB`–`0x0042E3D8` (길이 `29` bytes)
- VA: `0x000000014042E3BB`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A1B7C`
- 디코드: `4`개 명령, `29/29` bytes 표시
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
- `0x0042E3BB` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0042E3D3` → [sub_0042E13E + 0x1A7](Unknown_function_0042E13E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0042E3BB  48 8D 15 3E 1C BD FF            lea rdx, [rip - 0x42e3c2]
0042E3C2  41 0F B6 9C 13 70 C4 02 00      movzx ebx, byte ptr [r11 + rdx + 0x2c470]
0042E3CB  0F BF 84 5A 70 C7 02 00         movsx eax, word ptr [rdx + rbx*2 + 0x2c770]
0042E3D3  E9 0D FF FF FF                  jmp 0x14042e2e5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0042E3BB(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_0042E3BB(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042E3BB&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0042E3BB[BB_0042E3BB]
```
