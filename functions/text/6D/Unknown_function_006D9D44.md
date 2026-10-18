# sub_006D9D44

- RVA: `0x006D9D44`–`0x006D9D5F` (길이 `27` bytes)
- VA: `0x00000001406D9D44`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065660`
- 디코드: `7`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D9D54` → [CcDeleteBcbs](../38/CcDeleteBcbs_function_00389BF0.md) (function, `0x00389BF0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006D9D4B` → [CcSetFileSizesEx + 0x1CE](../26/CcSetFileSizesEx_function_0026D070.md) (`tail-transfer`)
  - `0x006D9D5A` → [CcSetFileSizesEx + 0x1CE](../26/CcSetFileSizesEx_function_0026D070.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006D9D44  48 8D 46 10                     lea rax, [rsi + 0x10]
006D9D48  48 39 00                        cmp qword ptr [rax], rax
006D9D4B  0F 84 ED 34 B9 FF               je 0x14026d23e
006D9D51  48 8B CE                        mov rcx, rsi
006D9D54  E8 97 FE CA FF                  call 0x140389bf0
006D9D59  90                              nop
006D9D5A  E9 DF 34 B9 FF                  jmp 0x14026d23e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006D9D44(void)
{
    __int64 result;

    result = CcDeleteBcbs(v_rsi, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006D9D44(void)
{
    int64_t result;

    result = CcDeleteBcbs(local_rsi, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D9D44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D9D44[BB_006D9D44]
  bb_006D9D51[BB_006D9D51]
  bb_006D9D44 -->|fallthrough| bb_006D9D51
```
