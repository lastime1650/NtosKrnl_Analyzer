# sub_006E2698

- RVA: `0x006E2698`–`0x006E26B3` (길이 `27` bytes)
- VA: `0x00000001406E2698`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00078E90`
- 디코드: `7`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E269B` → [KeAbCrossThreadDelete](../5C/KeAbCrossThreadDelete_function_005C517C.md) (function, `0x005C517C`)
- `0x006E26A8` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E26AE` → [KeDeleteMutant + 0xA2](../35/KeDeleteMutant_function_00351788.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E2698  48 8B D7                        mov rdx, rdi
006E269B  E8 DC 2A EE FF                  call 0x1405c517c
006E26A0  BA 44 66 6C 74                  mov edx, 0x746c6644
006E26A5  48 8B CF                        mov rcx, rdi
006E26A8  E8 33 52 C1 FF                  call 0x1402f78e0
006E26AD  90                              nop
006E26AE  E9 77 F1 C6 FF                  jmp 0x14035182a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E2698(void)
{
    __int64 result;

    result = KeAbCrossThreadDelete(a1, v_rdi, a3, a4);
    result = ObfDereferenceObjectWithTag(v_rdi, (unsigned int)(0x746C6644ULL), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006E2698(void)
{
    int64_t result;

    result = KeAbCrossThreadDelete(a1, local_rdi, a3, a4);
    result = ObfDereferenceObjectWithTag(local_rdi, (uint32_t)(0x746C6644ULL), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E2698&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E2698[BB_006E2698]
```
