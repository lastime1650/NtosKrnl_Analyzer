# sub_002F92CD

- RVA: `0x002F92CD`–`0x002F92E7` (길이 `26` bytes)
- VA: `0x00000001402F92CD`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000727E0`
- 디코드: `5`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002F92CD` → RVA `0x00E28F90` (`.data`; read)
- `0x002F92DB` → RVA `0x00E28FA4` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002F92D5` → [sub_002F908B](Unknown_function_002F908B.md) (`tail-transfer`)
  - `0x002F92E2` → [sub_002F908B](Unknown_function_002F908B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002F92CD  8B 05 BD FC B2 00               mov eax, dword ptr [rip + 0xb2fcbd]
002F92D3  85 C0                           test eax, eax
002F92D5  0F 8E B0 FD FF FF               jle 0x1402f908b
002F92DB  F0 FF 05 C2 FC B2 00            lock inc dword ptr [rip + 0xb2fcc2]
002F92E2  E9 A4 FD FF FF                  jmp 0x1402f908b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002F92CD(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_002F92CD(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F92CD&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002F92CD[BB_002F92CD]
  bb_002F92DB[BB_002F92DB]
  bb_002F92CD -->|fallthrough| bb_002F92DB
```
