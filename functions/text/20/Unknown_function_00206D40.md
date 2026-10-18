# sub_00206D40

- RVA: `0x00206D40`–`0x00206D61` (길이 `33` bytes)
- VA: `0x0000000140206D40`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CFA4`
- 디코드: `8`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00206D4C` → [KeDelayExecutionThread](KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00206D59` → [sub_002067E0 + 0x6C](Unknown_function_002067E0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00206D40  4C 8D 84 24 98 00 00 00         lea r8, [rsp + 0x98]
00206D48  33 D2                           xor edx, edx
00206D4A  33 C9                           xor ecx, ecx
00206D4C  E8 FF 27 00 00                  call 0x140209550
00206D51  8B 83 A8 1D 00 00               mov eax, dword ptr [rbx + 0x1da8]
00206D57  85 C0                           test eax, eax
00206D59  0F 84 ED FA FF FF               je 0x14020684c
00206D5F  EB DF                           jmp 0x140206d40
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00206D40(int a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19)
{
    __int64 result;

    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, a19, a4);
    goto loc_00206D40;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00206D40(int32_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, int64_t Arg19)
{
    int64_t result;

    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, Arg19, Arg4);
    goto loc_00206D40;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00206D40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00206D40[BB_00206D40]
  bb_00206D5F[BB_00206D5F]
  bb_00206D40 -->|fallthrough| bb_00206D5F
  bb_00206D5F -->|branch| bb_00206D40
```
