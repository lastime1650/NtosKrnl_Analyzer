# NtConnectPort

- RVA: `0x009229F0`–`0x00922A37` (길이 `71` bytes)
- VA: `0x00000001409229F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC98`
- 디코드: `15`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00922A2C` → [NtSecureConnectPort](NtSecureConnectPort_function_00922F20.md) (function, `0x00922F20`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009229F0  4C 8B DC                        mov r11, rsp
009229F3  48 83 EC 58                     sub rsp, 0x58
009229F7  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
009229FF  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00922A03  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
00922A0B  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00922A0F  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00922A17  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00922A1B  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00922A23  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
00922A27  49 83 63 C8 00                  and qword ptr [r11 - 0x38], 0
00922A2C  E8 EF 04 00 00                  call 0x140922f20
00922A31  48 83 C4 58                     add rsp, 0x58
00922A35  C3                              ret
00922A36  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtConnectPort(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (88);
    *(unsigned __int64 *)(v_rsp - 24) = a8;
    *(unsigned __int64 *)(v_rsp - 32) = a7;
    *(unsigned __int64 *)(v_rsp - 40) = a6;
    *(unsigned __int64 *)(v_rsp - 48) = a5;
    result = NtSecureConnectPort(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtConnectPort(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (88);
    *(uint64_t *)(local_rsp - 0x18) = Arg8;
    *(uint64_t *)(local_rsp - 0x20) = Arg7;
    *(uint64_t *)(local_rsp - 0x28) = Arg6;
    *(uint64_t *)(local_rsp - 0x30) = Arg5;
    result = NtSecureConnectPort(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009229F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009229F0[BB_009229F0]
  bb_00922A36[BB_00922A36]
```
