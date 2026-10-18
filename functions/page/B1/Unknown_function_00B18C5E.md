# sub_00B18C5E

- RVA: `0x00B18C5E`–`0x00B18C8F` (길이 `49` bytes)
- VA: `0x0000000140B18C5E`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007C4B0`
- 디코드: `14`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B18C7A` → [MiDereferenceEnclaveModule](../80/MiDereferenceEnclaveModule_function_008089B4.md) (function, `0x008089B4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B18C83` → [sub_0087FFB4 + 0x102](../87/Unknown_function_0087FFB4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B18C5E  48 8B 0B                        mov rcx, qword ptr [rbx]
00B18C61  48 39 59 08                     cmp qword ptr [rcx + 8], rbx
00B18C65  75 21                           jne 0x140b18c88
00B18C67  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00B18C6B  48 39 18                        cmp qword ptr [rax], rbx
00B18C6E  75 18                           jne 0x140b18c88
00B18C70  48 89 08                        mov qword ptr [rax], rcx
00B18C73  48 89 41 08                     mov qword ptr [rcx + 8], rax
00B18C77  48 8B CB                        mov rcx, rbx
00B18C7A  E8 35 FD CE FF                  call 0x1408089b4
00B18C7F  48 8B 5D A7                     mov rbx, qword ptr [rbp - 0x59]
00B18C83  E9 2E 74 D6 FF                  jmp 0x1408800b6
00B18C88  B9 03 00 00 00                  mov ecx, 3
00B18C8D  CD 29                           int 0x29
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B18C5E(void)
{
    __int64 result;

    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx) + 8)) != v_rbx) goto loc_00B18C88;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8))) != v_rbx) goto loc_00B18C88;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8)) = *(unsigned __int64 *)(v_rbx);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx) + 8) = *(unsigned __int64 *)(v_rbx + 8);
    result = MiDereferenceEnclaveModule(v_rbx, a2, a3, a4);
loc_00B18C88:
    return result;
}
```

## 5. (Beta) C Style

```c
void sub_00B18C5E(void)
{
    int64_t result;

    if ((*(uint64_t *)(*(uint64_t *)(local_rbx) + 0x8)) != local_rbx) goto loc_00B18C88;
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8))) != local_rbx) goto loc_00B18C88;
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x8)) = *(uint64_t *)(local_rbx);
    *(uint64_t *)(*(uint64_t *)(local_rbx) + 0x8) = *(uint64_t *)(local_rbx + 0x8);
    result = MiDereferenceEnclaveModule(local_rbx, a2, a3, a4);
loc_00B18C88:
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B18C5E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B18C5E[BB_00B18C5E]
  bb_00B18C67[BB_00B18C67]
  bb_00B18C70[BB_00B18C70]
  bb_00B18C88[BB_00B18C88]
  bb_00B18C5E -->|branch| bb_00B18C88
  bb_00B18C5E -->|fallthrough| bb_00B18C67
  bb_00B18C67 -->|branch| bb_00B18C88
  bb_00B18C67 -->|fallthrough| bb_00B18C70
```
