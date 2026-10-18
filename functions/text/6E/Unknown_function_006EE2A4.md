# sub_006EE2A4

- RVA: `0x006EE2A4`–`0x006EE2C3` (길이 `31` bytes)
- VA: `0x00000001406EE2A4`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A0FCC`
- 디코드: `5`개 명령, `31/31` bytes 표시
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
  - `0x006EE2BE` → [HvlMapSparseGpaPages + 0x7D](../42/HvlMapSparseGpaPages_function_0042A160.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006EE2A4  88 45 E8                        mov byte ptr [rbp - 0x18], al
006EE2A7  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
006EE2B0  C7 45 EC 01 00 00 00            mov dword ptr [rbp - 0x14], 1
006EE2B7  48 8B 80 00 8C 00 00            mov rax, qword ptr [rax + 0x8c00]
006EE2BE  E9 1A BF D3 FF                  jmp 0x14042a1dd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006EE2A4(void)
{
    *(unsigned __int8 *)(v_rbp - 24) = (unsigned __int8)(result);
    *(unsigned int *)(v_rbp - 20) = 1;
}
```

## 5. (Beta) C Style

```c
void sub_006EE2A4(void)
{
    *(uint8_t *)(local_rbp - 0x18) = (uint8_t)(result);
    *(uint32_t *)(local_rbp - 0x14) = 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006EE2A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006EE2A4[BB_006EE2A4]
```
