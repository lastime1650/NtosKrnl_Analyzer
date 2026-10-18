# SeSetImageBaseAddress

- RVA: `0x00AA8898`–`0x00AA88BA` (길이 `34` bytes)
- VA: `0x0000000140AA8898`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `10`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AA88A8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [MiRelocateImageAgain](../98/MiRelocateImageAgain_function_009885C8.md) at `0x0098879A`
- [MiCaptureSecureImageBaseAddress](MiCaptureSecureImageBaseAddress_function_00AA881C.md) at `0x00AA8865`
- [sub_00B2B6D0](../B2/Unknown_function_00B2B6D0.md) at `0x00B2B776`

### Static image references
- `0x00AA889C` → RVA `0x00F04EC0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AA88A8` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA8898  48 83 EC 28                     sub rsp, 0x28
00AA889C  48 8B 05 1D C6 45 00            mov rax, qword ptr [rip + 0x45c61d]
00AA88A3  48 85 C0                        test rax, rax
00AA88A6  74 0B                           je 0x140aa88b3
00AA88A8  E8 23 22 C1 FF                  call 0x1406baad0
00AA88AD  48 83 C4 28                     add rsp, 0x28
00AA88B1  C3                              ret
00AA88B2  CC                              int3
00AA88B3  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00AA88B8  EB F3                           jmp 0x140aa88ad
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeSetImageBaseAddress(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 4572701) == 0) goto loc_00AA88B3;
    result = guard_dispatch_icall(a1, a2, a3, a4);
loc_00AA88AD:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00AA88B3:
    goto loc_00AA88AD;
}
```

## 5. (Beta) C Style

```c
void SeSetImageBaseAddress(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x45C61D) == 0) goto loc_00AA88B3;
    result = guard_dispatch_icall(a1, a2, a3, a4);
loc_00AA88AD:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00AA88B3:
    goto loc_00AA88AD;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA8898&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA8898[BB_00AA8898]
  bb_00AA88A8[BB_00AA88A8]
  bb_00AA88AD[BB_00AA88AD]
  bb_00AA88B2[BB_00AA88B2]
  bb_00AA88B3[BB_00AA88B3]
  bb_00AA8898 -->|branch| bb_00AA88B3
  bb_00AA8898 -->|fallthrough| bb_00AA88A8
  bb_00AA88A8 -->|flow| bb_00AA88AD
  bb_00AA88B2 -->|flow| bb_00AA88B3
  bb_00AA88B3 -->|branch| bb_00AA88AD
```
