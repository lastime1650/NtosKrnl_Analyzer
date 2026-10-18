# sub_00332AE1

- RVA: `0x00332AE1`–`0x00332B01` (길이 `32` bytes)
- VA: `0x0000000140332AE1`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000766C0`
- 디코드: `7`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00332AF7` → [MiFlushSingleTbEntry](../28/MiFlushSingleTbEntry_function_0028E730.md) (function, `0x0028E730`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00332AE1` → RVA `0x00010880` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00332AFC` → [sub_003329BC + 0x56](Unknown_function_003329BC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00332AE1  48 8B 05 98 DD CD FF            mov rax, qword ptr [rip - 0x322268]
00332AE8  BA 02 00 00 00                  mov edx, 2
00332AED  48 8B CB                        mov rcx, rbx
00332AF0  49 89 07                        mov qword ptr [r15], rax
00332AF3  44 8D 42 FF                     lea r8d, [rdx - 1]
00332AF7  E8 34 BC F5 FF                  call 0x14028e730
00332AFC  E9 11 FF FF FF                  jmp 0x140332a12
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00332AE1(void)
{
    __int64 result;

    *(unsigned __int64 *)(v_r15) = *(unsigned __int64 *)(v_rip - 3285608);
    result = MiFlushSingleTbEntry(v_rbx, 2, 2 - 1, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00332AE1(void)
{
    int64_t result;

    *(uint64_t *)(local_r15) = *(uint64_t *)(v_rip - 0x322268);
    result = MiFlushSingleTbEntry(local_rbx, 2, 2 - 1, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00332AE1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00332AE1[BB_00332AE1]
```
