# sub_00B3A7D8

- RVA: `0x00B3A7D8`–`0x00B3A7EA` (길이 `18` bytes)
- VA: `0x0000000140B3A7D8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AE8A4`
- 디코드: `3`개 명령, `18/18` bytes 표시
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
- `0x00B3A7D8` → RVA `0x00E0EEA8` (`.data`; write)
- `0x00B3A7DE` → RVA `0x00EEFEC0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B3A7E5` → [BiGetFirmwareType + 0x39](../A3/BiGetFirmwareType_function_00A3FA5C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B3A7D8  89 1D CA 46 2D 00               mov dword ptr [rip + 0x2d46ca], ebx
00B3A7DE  C6 05 DB 56 3B 00 01            mov byte ptr [rip + 0x3b56db], 1
00B3A7E5  E9 AB 52 F0 FF                  jmp 0x140a3fa95
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00B3A7D8(void)
{
    *(unsigned int *)(v_rip + 2967242) = (unsigned int)(v_rbx);
    *(unsigned __int8 *)(v_rip + 3888859) = 1;
}
```

## 5. (Beta) C Style

```c
void sub_00B3A7D8(void)
{
    *(uint32_t *)(v_rip + 0x2D46CA) = (uint32_t)(local_rbx);
    *(uint8_t *)(v_rip + 0x3B56DB) = 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B3A7D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B3A7D8[BB_00B3A7D8]
```
