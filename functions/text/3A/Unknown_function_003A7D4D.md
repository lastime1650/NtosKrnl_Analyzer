# sub_003A7D4D

- RVA: `0x003A7D4D`–`0x003A7D7A` (길이 `45` bytes)
- VA: `0x00000001403A7D4D`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00089CA8`
- 디코드: `8`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003A7D64` → [SepGetProcUniqueLuidAndIndexFromAttributeInfo](../30/SepGetProcUniqueLuidAndIndexFromAttributeInfo_function_00300A78.md) (function, `0x00300A78`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003A7D6B` → [sub_003A7AB1 + 0x6A](Unknown_function_003A7AB1.md) (`tail-transfer`)
  - `0x003A7D75` → [sub_003A7C07 + 0x55](Unknown_function_003A7C07.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003A7D4D  48 8B 8E 08 03 00 00            mov rcx, qword ptr [rsi + 0x308]
003A7D54  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
003A7D5C  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
003A7D64  E8 0F 8D F5 FF                  call 0x140300a78
003A7D69  8B E8                           mov ebp, eax
003A7D6B  E9 AB FD FF FF                  jmp 0x1403a7b1b
003A7D70  BD 17 00 00 C0                  mov ebp, 0xc0000017
003A7D75  E9 E2 FE FF FF                  jmp 0x1403a7c5c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003A7D4D(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17)
{
    __int64 result;

    result = SepGetProcUniqueLuidAndIndexFromAttributeInfo(*(unsigned __int64 *)(v_rsi + 776), a17, a16, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_003A7D4D(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, int64_t Arg16, int64_t Arg17)
{
    int64_t result;

    result = SepGetProcUniqueLuidAndIndexFromAttributeInfo(*(uint64_t *)(local_rsi + 0x308), Arg17, Arg16, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A7D4D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003A7D4D[BB_003A7D4D]
  bb_003A7D70[BB_003A7D70]
```
