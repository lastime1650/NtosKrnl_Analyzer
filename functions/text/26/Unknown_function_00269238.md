# sub_00269238

- RVA: `0x00269238`–`0x0026925A` (길이 `34` bytes)
- VA: `0x0000000140269238`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000652C8`
- 디코드: `8`개 명령, `34/34` bytes 표시
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
  - `0x00269255` → [SmHpBufferUpdateFullness + 0x56](SmHpBufferUpdateFullness_function_002690B0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00269238  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
0026923D  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00269242  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
00269247  48 89 3E                        mov qword ptr [rsi], rdi
0026924A  48 89 46 08                     mov qword ptr [rsi + 8], rax
0026924E  48 89 30                        mov qword ptr [rax], rsi
00269251  48 89 77 08                     mov qword ptr [rdi + 8], rsi
00269255  E9 AC FE FF FF                  jmp 0x140269106
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00269238(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15)
{
    *(unsigned __int64 *)(v_rsi) = v_rdi;
    *(unsigned __int64 *)(v_rsi + 8) = result;
    *(unsigned __int64 *)(result) = v_rsi;
    *(unsigned __int64 *)(v_rdi + 8) = v_rsi;
}
```

## 5. (Beta) C Style

```c
void sub_00269238(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, int64_t Arg13, uint64_t Arg14, int64_t Arg15)
{
    *(uint64_t *)(local_rsi) = local_rdi;
    *(uint64_t *)(local_rsi + 0x8) = result;
    *(uint64_t *)(result) = local_rsi;
    *(uint64_t *)(local_rdi + 0x8) = local_rsi;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00269238&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00269238[BB_00269238]
```
