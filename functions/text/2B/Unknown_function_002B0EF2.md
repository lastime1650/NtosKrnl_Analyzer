# sub_002B0EF2

- RVA: `0x002B0EF2`–`0x002B0F0E` (길이 `28` bytes)
- VA: `0x00000001402B0EF2`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006D5EC`
- 디코드: `6`개 명령, `28/28` bytes 표시
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
- `0x002B0EF2` → RVA `0x00FC6CF8` (`ALMOSTRO`; read)
- `0x002B0F00` → RVA `0x00FC5088` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002B0EFB` → [MiClearStackOwners + 0x30](MiClearStackOwners_function_002B0D90.md) (`tail-transfer`)
  - `0x002B0F09` → [MiClearStackOwners + 0x30](MiClearStackOwners_function_002B0D90.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002B0EF2  8B 15 00 5E D1 00               mov edx, dword ptr [rip + 0xd15e00]
002B0EF8  C1 EA 0C                        shr edx, 0xc
002B0EFB  E9 C0 FE FF FF                  jmp 0x1402b0dc0
002B0F00  8B 15 82 41 D1 00               mov edx, dword ptr [rip + 0xd14182]
002B0F06  C1 EA 0C                        shr edx, 0xc
002B0F09  E9 B2 FE FF FF                  jmp 0x1402b0dc0
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_002B0EF2(void)
{
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 13721088))) >> (12));
}
```

## 5. (Beta) C Style

```c
void sub_002B0EF2(void)
{
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xD15E00))) >> (12));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002B0EF2&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002B0EF2[BB_002B0EF2]
  bb_002B0F00[BB_002B0F00]
```
