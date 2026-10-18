# sub_00B3F31A

- RVA: `0x00B3F31A`–`0x00B3F334` (길이 `26` bytes)
- VA: `0x0000000140B3F31A`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B43BC`
- 디코드: `4`개 명령, `26/26` bytes 표시
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
- `0x00B3F325` → RVA `0x00E67B0C` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00B3F31F` → [RtlpGetTimeZoneInfoHandle + 0x4F](../A6/RtlpGetTimeZoneInfoHandle_function_00A6BD8C.md) (`tail-transfer`)
  - `0x00B3F32F` → [RtlpGetTimeZoneInfoHandle + 0x38](../A6/RtlpGetTimeZoneInfoHandle_function_00A6BD8C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B3F31A  3D 34 00 00 C0                  cmp eax, 0xc0000034
00B3F31F  0F 85 B6 CA F2 FF               jne 0x140a6bddb
00B3F325  C7 05 DD 87 32 00 02 00 00 00   mov dword ptr [rip + 0x3287dd], 2
00B3F32F  E9 90 CA F2 FF                  jmp 0x140a6bdc4
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00B3F31A(void)
{
    *(unsigned int *)(v_rip + 3311581) = 2;
}
```

## 5. (Beta) C Style

```c
void sub_00B3F31A(void)
{
    *(uint32_t *)(v_rip + 0x3287DD) = 2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B3F31A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B3F31A[BB_00B3F31A]
  bb_00B3F325[BB_00B3F325]
  bb_00B3F31A -->|fallthrough| bb_00B3F325
```
