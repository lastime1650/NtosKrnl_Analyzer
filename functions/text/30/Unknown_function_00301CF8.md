# sub_00301CF8

- RVA: `0x00301CF8`–`0x00301D13` (길이 `27` bytes)
- VA: `0x0000000140301CF8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073214`
- 디코드: `6`개 명령, `27/27` bytes 표시
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
  - `0x00301D11` → [sub_00301D13 + 0x1C](Unknown_function_00301D13.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00301CF8  89 2B                           mov dword ptr [rbx], ebp
00301CFA  44 88 6B 04                     mov byte ptr [rbx + 4], r13b
00301CFE  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
00301D06  48 8B AC 24 A0 00 00 00         mov rbp, qword ptr [rsp + 0xa0]
00301D0E  45 84 C0                        test r8b, r8b
00301D11  74 1C                           je 0x140301d2f
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00301CF8(__int64 a1, __int64 a2, unsigned __int8 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20)
{
    *(unsigned int *)(v_rbx) = (unsigned int)(v_rbp);
    *(unsigned __int8 *)(v_rbx + 4) = (unsigned __int8)(v_r13);
}
```

## 5. (Beta) C Style

```c
void sub_00301CF8(int64_t Arg1, int64_t Arg2, uint8_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, int64_t Arg18, uint64_t Arg19, int64_t Arg20)
{
    *(uint32_t *)(local_rbx) = (uint32_t)(local_rbp);
    *(uint8_t *)(local_rbx + 0x4) = (uint8_t)(local_r13);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00301CF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00301CF8[BB_00301CF8]
```
