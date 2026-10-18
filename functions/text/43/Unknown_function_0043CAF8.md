# sub_0043CAF8

- RVA: `0x0043CAF8`–`0x0043CB13` (길이 `27` bytes)
- VA: `0x000000014043CAF8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A467C`
- 디코드: `6`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0043CB09` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0043CAFB` → [sub_0043C9E8 + 0x6D](Unknown_function_0043C9E8.md) (`tail-transfer`)
  - `0x0043CB0E` → [sub_0043C9E8 + 0x6D](Unknown_function_0043C9E8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0043CAF8  45 85 E4                        test r12d, r12d
0043CAFB  0F 85 54 FF FF FF               jne 0x14043ca55
0043CB01  BA 44 66 6C 74                  mov edx, 0x746c6644
0043CB06  49 8B CE                        mov rcx, r14
0043CB09  E8 02 3C DD FF                  call 0x140210710
0043CB0E  E9 42 FF FF FF                  jmp 0x14043ca55
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0043CAF8(void)
{
    __int64 result;

    result = ObfReferenceObjectWithTag(v_r14, (unsigned int)(0x746C6644ULL), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0043CAF8(void)
{
    int64_t result;

    result = ObfReferenceObjectWithTag(local_r14, (uint32_t)(0x746C6644ULL), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043CAF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043CAF8[BB_0043CAF8]
  bb_0043CB01[BB_0043CB01]
  bb_0043CAF8 -->|fallthrough| bb_0043CB01
```
