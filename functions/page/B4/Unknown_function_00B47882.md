# sub_00B47882

- RVA: `0x00B47882`–`0x00B478B4` (길이 `50` bytes)
- VA: `0x0000000140B47882`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B998C`
- 디코드: `12`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B478A8` → [MiUpdateVadBits](../A8/MiUpdateVadBits_function_00A8DAC8.md) (function, `0x00A8DAC8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B47895` → RVA `0x00E2F388` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B478AF` → [MiExpandVadBitMapDown + 0xA7](../A9/MiExpandVadBitMapDown_function_00A95EC4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B47882  33 C0                           xor eax, eax
00B47884  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00B47888  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
00B4788C  48 83 63 18 00                  and qword ptr [rbx + 0x18], 0
00B47891  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00B47895  48 2B 0D EC 7A 2E 00            sub rcx, qword ptr [rip + 0x2e7aec]
00B4789C  48 C1 E1 13                     shl rcx, 0x13
00B478A0  48 C1 E7 1F                     shl rdi, 0x1f
00B478A4  48 8D 14 39                     lea rdx, [rcx + rdi]
00B478A8  E8 1B 62 F4 FF                  call 0x140a8dac8
00B478AD  8B C5                           mov eax, ebp
00B478AF  E9 B7 E6 F4 FF                  jmp 0x140a95f6b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B47882(void)
{
    __int64 result;
    __int64 v_rdi;

    result = 0;
    *(unsigned __int64 *)(v_rbx + 16) = 0;
    *(unsigned __int64 *)(v_rbx + 32) = 0;
    a1 = (*(unsigned __int64 *)(v_rbx + 8)) - (*(unsigned __int64 *)(v_rip + 3046124));
    a1 = (a1) << (19);
    v_rdi = (v_rdi) << (31);
    result = MiUpdateVadBits(a1, a1 + v_rdi * 1, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B47882(void)
{
    int64_t result;
    int64_t local_rdi;

    result = 0;
    *(uint64_t *)(local_rbx + 0x10) = 0;
    *(uint64_t *)(local_rbx + 0x20) = 0;
    a1 = (*(uint64_t *)(local_rbx + 0x8)) - (*(uint64_t *)(v_rip + 0x2E7AEC));
    a1 = (a1) << (19);
    local_rdi = (local_rdi) << (31);
    result = MiUpdateVadBits(a1, a1 + local_rdi * 1, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B47882&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B47882[BB_00B47882]
```
