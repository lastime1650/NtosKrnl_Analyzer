# sub_003136CC

- RVA: `0x003136CC`–`0x003136E0` (길이 `20` bytes)
- VA: `0x00000001403136CC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000745F4`
- 디코드: `5`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003136D9` → [EtwGetKernelTraceTimestamp](../39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003136DE` → [sub_00313654 + 0x29](Unknown_function_00313654.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003136CC  BA 10 00 00 A0                  mov edx, 0xa0000010
003136D1  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
003136D6  40 B7 01                        mov dil, 1
003136D9  E8 72 C5 08 00                  call 0x14039fc50
003136DE  EB 9D                           jmp 0x14031367d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003136CC(void)
{
    __int64 result;
    unsigned __int64 v_stack_p20;

    result = EtwGetKernelTraceTimestamp(v_stack_p20, (unsigned int)(0xA0000010ULL), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_003136CC(void)
{
    int64_t result;
    uint64_t v_stack_p20;

    result = EtwGetKernelTraceTimestamp(v_stack_p20, (uint32_t)(0xA0000010ULL), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003136CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003136CC[BB_003136CC]
```
